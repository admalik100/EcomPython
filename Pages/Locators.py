# user Def helper function to find elements in cases where same id/class used for multiple elements
class ElemLocators:

    def by_css_containing_text(driver, selector, text):
        elements = driver.find_elements_by_css_selector(selector)
        return [element for element in elements
                if text in (element.text or
                            element.get_attribute("textContent") or
                            element.get_attribute("innerText"))]

