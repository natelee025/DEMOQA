# Chrome
def test_select_file(elements_ch):
    elements_ch.to_check_box()
    elements_ch.open_dir_home()
    elements_ch.open_dir_downloads()
    elements_ch.select_word_file()
    elements_ch.assert_selected_file()
