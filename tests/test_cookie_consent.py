def test_cookie_consent(playwright, browser_name):
    browser = getattr(playwright, browser_name).launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.ing.pl/")  

    page.get_by_role("button", name="Dostosuj").click()
    page.get_by_role("switch", name="Cookies analityczne").locator("span").first.click()
    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()
    page.reload()
    page.get_by_role("link", name="Przedsiębiorcy").click()
    page.get_by_role("link", name="Premium").click()


    cookies = context.cookies()
    analytics_cookies = [
        c for c in cookies
        if c["name"].startswith("_ga")
        or c["name"].startswith("AMCV")
        or c["name"] == "s_cc"
    ]
    policy_cookie = next((c for c in cookies if c["name"] == "cookiePolicyGDPR"), None)
    
    # Checking if policy was set correctly
    assert policy_cookie is not None, "cookiePolicyGDPR not found!"
    assert policy_cookie["value"] == "3", f"Unexpected value for cookiePolicyGDPR: {policy_cookie['value']}"

    # Checking if there are analytics cookies 
    assert analytics_cookies, "No analytics cookies found after consent!"

    browser.close()
