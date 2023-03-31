# Firefox
def test_select_file(elements_fx):
    elements_fx.to_check_box()
    elements_fx.open_dir_home()
    elements_fx.open_dir_downloads()
    elements_fx.select_word_file()
    elements_fx.assert_selected_file()
