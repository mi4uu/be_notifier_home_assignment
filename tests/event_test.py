from copy import copy
from be_notifier.entities import Event, CRAWLING_STATUSES
from be_notifier.notify import notify


def test_new_event():
    new = Event(
        start_date="2020-01-01",
        description="test",
        location="test",
        name="xxx",
        link="xxxxxxx",
    )
    old = None
    result = notify(new, old)

    assert result == new

def test_deleted_event():
    old = Event(
        start_date="2020-01-01",
        description="test",
        location="test",
        name="xxx",
        link="xxxxxxx",
    )
    new = None
    result = notify(new, old)

    assert result == new

def test_same_event():
    old = Event(
        start_date="2020-01-01",
        description="test",
        location="test",
        name="xxx",
        link="xxxxxxx",
    )
    new = Event(
        start_date="2020-01-01",
        description="test",
        location="test",
        name="xxx",
        link="xxxxxxx",
    )
    result = notify(new, old)

    assert result == False

def test_event_with_changes_that_doesnt_matter():
    old = Event(
        start_date="2020-01-01",
        description="test",
        location="test",
        name="xxx",
        link="xxxxxxx",
    )
    new = Event(
        start_date="2022-01-01",
        end_date="2022-01-01",
        description="Somewhere over the rainbow",
        location="Arizona",
        name="nova",
        link="no link provided",
    )
    result = notify(new, old)

    assert result == False



def test_event_with_delete_status_changed():
    old = Event(
        start_date="2020-01-01",
        description="test",
        location="test",
        name="xxx",
        link="xxxxxxx",
    )
    new = copy(old)
    new.is_deleted = True
    result = notify(new, old)

    assert result == new


def test_event_with_crawling_status_changed():
    old = Event(
        start_date="2020-01-01",
        description="test",
        location="test",
        name="xxx",
        link="xxxxxxx",
    )
    new = copy(old)
    new.crawling_status = CRAWLING_STATUSES.AWAITING_CRAWL

    assert notify(new, old) == False
    
    new.crawling_status = CRAWLING_STATUSES.TEXT_ANALYZED
    
    assert notify(new, old) == new



