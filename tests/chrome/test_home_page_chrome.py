# Chrome
def test_go_to_elements_pages(home_ch):
    home_ch.to_elements_page()
    home_ch.assert_message()
