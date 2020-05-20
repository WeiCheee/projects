from PyQt5.QtGui import QTextCursor

def update_content(self):
    new_content = self.terminal.read()
    new_content = self.process_backspaces(new_content)
    if not new_content:
        return

    scrollbar = self.outputTextEdit.verticalScrollBar()
    assert isinstance(scrollbar, QScrollBar)
    # Preserve scroll while updating content
    current_scroll = scrollbar.value()

    prev_cursor = self.outputTextEdit.textCursor()
    self.outputTextEdit.moveCursor(QTextCursor.End)
    # Use any backspaces that were left in input to delete text
    cut = 0
    for x in new_content:
        if x != "\b":
            break
        self.outputTextEdit.textCursor().deletePreviousChar()
        cut += 1
    self.outputTextEdit.insertPlainText(new_content[cut:])
    self.outputTextEdit.setTextCursor(prev_cursor)

    if self._auto_scroll:
        scrollbar.setValue(scrollbar.maximum())
    else:
        scrollbar.setValue(current_scroll) 
