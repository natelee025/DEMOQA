# Firefox
def test_go_to_elements_pages(home_fx):
    home_fx.to_elements_page()
    home_fx.assert_message()
