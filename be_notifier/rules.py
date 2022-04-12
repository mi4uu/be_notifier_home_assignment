from typing import Callable, List, Optional, Union
from be_notifier.entities import CRAWLING_STATUSES, Entity
from be_notifier.entities import (
    Company,
    CompanyCompetitor,
    CompanyForEvent,
    CompanyForWebinar,
    ContentItem,
    Event,
    Webinar,
)


def is_new_filter(_: Optional[Entity], old: Optional[Entity]) -> bool:
    return old is None


def is_deleted_filter(new: Optional[Entity], _: Optional[Entity]) -> bool:
    return new is None


def is_delete_has_changed_filter(new: Entity, old: Entity) -> bool:
    return new.is_deleted != old.is_deleted


def crawling_status_has_changed_filter(new: Entity, old: Entity) -> bool:
    return new.crawling_status != old.crawling_status and new.crawling_status in [
        CRAWLING_STATUSES.TEXT_ANALYZED,
        CRAWLING_STATUSES.TEXT_UPLOADED,
    ]


def is_blacklisted_has_changed_filter(new: Entity, old: Entity) -> bool:
    return new.is_blacklisted != old.is_blacklisted


def return_target_new(new: Entity, _: Entity) -> Entity:
    return new


def return_target_company(
    new: Union[CompanyCompetitor, CompanyForWebinar, ContentItem], _: Entity
) -> Entity:
    return new.company


def return_target_event(new: CompanyForEvent, _: Entity) -> Entity:
    return new.event


RulesType = List[Callable[[Optional[Entity], Optional[Entity]], bool]]
TargetType = Callable[[Optional[Entity], Optional[Entity]], Optional[Entity]]

RULES = {
    Company: {
        "rules": [
            is_new_filter,
            is_deleted_filter,
            is_delete_has_changed_filter,
            crawling_status_has_changed_filter,
        ],
        "target": return_target_new,
    },
    Webinar: {
        "rules": [
            is_new_filter,
            is_deleted_filter,
            is_delete_has_changed_filter,
            crawling_status_has_changed_filter,
            is_blacklisted_has_changed_filter,
        ],
        "target": return_target_new,
    },
    Event: {
        "rules": [
            is_new_filter,
            is_deleted_filter,
            is_delete_has_changed_filter,
            crawling_status_has_changed_filter,
            is_blacklisted_has_changed_filter,
        ],
        "target": return_target_new,
    },
    ContentItem: {
        "rules": [
            is_new_filter,
            is_deleted_filter,
            is_delete_has_changed_filter,
            crawling_status_has_changed_filter,
            is_blacklisted_has_changed_filter,
        ],
        "target": return_target_company,
    },
    CompanyForEvent: {
        "rules": [
            is_new_filter,
            is_deleted_filter,
            is_delete_has_changed_filter,
            is_blacklisted_has_changed_filter,
        ],
        "target": return_target_event,
    },
    CompanyForWebinar: {
        "rules": [
            is_new_filter,
            is_deleted_filter,
            is_delete_has_changed_filter,
            is_blacklisted_has_changed_filter,
        ],
        "target": return_target_company,
    },
    CompanyCompetitor: {
        "rules": [
            is_new_filter,
            is_deleted_filter,
            is_delete_has_changed_filter,
        ],
        "target": return_target_company,
    },
}
