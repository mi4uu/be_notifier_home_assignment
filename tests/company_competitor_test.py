from copy import copy
from be_notifier.entities import CompanyCompetitor,Company
from be_notifier.notify import notify


def test_new_company_competitor():
    company = Company(employees_min=1, employees_max=3, link="http://fb.com", name="Facebook")
    competitor = Company(employees_min=5, employees_max=15,  link="https://www.google.com", name="Google")
    
    new = CompanyCompetitor(
        company=company,
        competitor=competitor,
       
    )
    old = None
    result = notify(new, old)

    assert result == new.company
    
def test_same_company_competitor():
    company = Company(employees_min=1, employees_max=3, link="http://fb.com", name="Facebook")
    competitor = Company(employees_min=5, employees_max=15,  link="https://www.google.com", name="Google")
    
    old = CompanyCompetitor(
        company=company,
        competitor=competitor,
       
    )
    new = copy(old)
    result = notify(new, old)

    assert result == False
    
def test_company_competitor_is_deleted():
    company = Company(employees_min=1, employees_max=3, link="http://fb.com", name="Facebook")
    competitor = Company(employees_min=5, employees_max=15,  link="https://www.google.com", name="Google")
    
    old = CompanyCompetitor(
        company=company,
        competitor=competitor,
       
    )
    new = copy(old)
    new.is_deleted = True
    result = notify(new, old)

    assert result == new.company
