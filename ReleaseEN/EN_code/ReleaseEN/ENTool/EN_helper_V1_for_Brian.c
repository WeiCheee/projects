#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int Dirname();
void Parse(char FRF_filename[]);
int Search(char dirname[]);
char *PartNo(char dirname[]);

char dir[500][300];
int dir_num;

int main()
{
    char szDir[300],InputPath[300] = "_FRF\\",run[300];
    int t=0;

    printf("                   ------------------------------\n");
    printf("                   |      EN Helper for CV1      |\n");
    printf("                   ------------------------------\n");

    dir_num = Dirname();
    remove("message.txt");

    sprintf(run,"del _rar\\*.rar");
    system(run);

    WIN32_FIND_DATA FileData;
    HANDLE          hList;
    sprintf(szDir,"%s\\*", InputPath );
    if ( (hList = FindFirstFile(szDir,&FileData))==INVALID_HANDLE_VALUE )
        printf("No files be found.\n\n");
    else
    {
        while (1)
        {
            if (!FindNextFile( hList , &FileData ))
            {
                if (GetLastError() == ERROR_NO_MORE_FILES)
                    break;
            }
            if( t>0 )
            {
                //printf("%s\n",FileData.cFileName);
                if( strstr(FileData.cFileName,"_FRF") )
                    Parse( FileData.cFileName );
                else
                    printf("Check the File Name have \"FRF\"\n");
            }
            t++;
        }
    }
    FindClose(hList);
    system("start message.txt");

    return 0;
}

int Dirname()
{
    char szDir[300];
    int t=0;

    WIN32_FIND_DATA FileData;
    HANDLE          hList;
    sprintf(szDir,"FWReleaseTool\\*");
    if ( (hList = FindFirstFile(szDir,&FileData)) == INVALID_HANDLE_VALUE )
        printf("Directory \"FWReleaseTool\" can not be found.\n\n");
    else
    {
        while (1)
        {
            if (!FindNextFile(hList, &FileData))
            {
                if (GetLastError() == ERROR_NO_MORE_FILES)
                    break;
            }
            if(t>0)
            {
                strcpy(dir[t],FileData.cFileName);
                //printf("%d. %s\n",t,dir[t]);
            }
            t++;
        }
    }
    FindClose(hList);

    return --t;
}

void Parse(char FRF_filename[])
{
    char *p;
    char FWname[500],temp[500];
    int status=0;

    strcpy(temp,FRF_filename);
    p = strtok(temp,"_");
    strcpy(FWname,p);

    status = Search( FWname );

    if( status==1 )
        printf("========================================\n");
    else
    {
        printf("== %s Fail ==\n\n========================================\n",FWname);
        system("pause");
    }
}

int Search(char dirname[])
{
    FILE *fwp,*frp;
    char szDir[300],run[300],temp[300],checksumtxt[300],sum[300];
    char *p,*Part_head;
    int i,flag=0;

    WIN32_FIND_DATA FileData;
    HANDLE          hList;

    for( i=1 ; i<=dir_num ; i++ )
    {
        sprintf(szDir,"FWReleaseTool\\%s\\%s",dir[i],dirname);
        if ( !(( hList = FindFirstFile( szDir , &FileData )) == INVALID_HANDLE_VALUE ))
        {
            printf("Find %s in \"%s\"\n",dirname,szDir);
            flag = 1;

            fwp = fopen("message.txt","a");

            strcpy(temp,dir[i]);
            p = strtok(temp,"_");
            strcpy(temp,p);

            fprintf(fwp,"%s\n",dirname);


            Part_head = PartNo(dirname);
            if( Part_head != NULL )
            {
                if( strlen(dirname)==8 )
                    fprintf(fwp,"%s%s\n",Part_head,dirname);
                else if( strlen(dirname)==7 )
                    fprintf(fwp,"%s%s0\n",Part_head,dirname);
                else
                {
                    printf("\tdirname : %s ERROR!!\n",dirname);
                }
            }

            fprintf(fwp,"Release FW %s for %s\n",dirname,temp);

            sprintf(run,"%s\\sChkSum.exe %s\\FW\\%s.bin > %s.txt",szDir,szDir,dirname,dirname);
            system(run);

            sprintf(checksumtxt,"%s.txt",dirname);
            frp = fopen(checksumtxt,"r");
            while ( fgets(sum,300,frp)!=NULL )
            {
            }
            fclose(frp);
            p = strtok(sum,".");
            strcpy(sum,p);

            fprintf(fwp,"%s\n\n",sum);
            fclose(fwp);

            remove(checksumtxt);

            sprintf(run,"start WinRAR.exe a -ep1 -ibck _rar\\%s_bin.rar %s\\FW\\%s.bin",dirname,szDir,dirname);
            system(run);
            printf("  %s_bin.rar create successfully\n",dirname);

            sprintf(run,"start WinRAR.exe a -ep1 -ibck _rar\\%s_dat.rar %s\\*.dat",dirname,szDir);
            system(run);
            printf("  %s_dat.rar create successfully\n",dirname);

            sprintf(run,"start WinRAR.exe a -ep1 -ibck _rar\\%s_FRF.rar _FRF\\%s_FRF.xls",dirname,dirname);
            system(run);
            printf("  %s_FRF.rar create successfully\n",dirname);

            sprintf(run,"WinRAR.exe a -ep1 _rar\\%s.rar %s",dirname,szDir);
            system(run);
            printf("  %s.rar create     successfully\n",dirname);

            FindClose(hList);
        }
    }
    if( !flag )
    {
        printf("Can not found %s in any directory\nPlease check it!\n",dirname);
        return 0;
    }
    return 1;
}

char *PartNo(char dirname[])
{
    FILE *frp_PartNo;
    char *p;
    char line[500],FF[50];

    frp_PartNo = fopen("CV1_PartNo.data","r");

    if( frp_PartNo )
    {
        while( fgets(line,500,frp_PartNo)!=NULL )
        {
            p = strtok(line,"\t");
            if(p)
            {
                strcpy( FF , p );
                if( FF[0]==dirname[0] && FF[1]==dirname[1] )
                {
                    p = strtok(NULL,"\n");

                    fclose(frp_PartNo);
                    return p;
                }
            }
        }
        printf("\"CV1_PartNo.data\" doesn't have %c%c 's FF\nPlease check it!!\n",dirname[0],dirname[1]);
        system("pause");
    }
    else
        printf("Can Not find \"CV1_PartNo.data\" !!\n Please check it!!\n");

    fclose(frp_PartNo);

    return NULL;
}
