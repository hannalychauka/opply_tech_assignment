from helpers.enums import ChoiceEnum


class AdditionalDetailsTypeEnum(ChoiceEnum):
    CREATED = 0
    IN_PROGRESS = 1
    IN_DELIVERY = 2
    DELIVERED = 3
    CANCELLED = 4
    DECLINED = 5

    messages = {
        CREATED: 'Order is created',
        IN_PROGRESS: 'Order is being prepared',
        IN_DELIVERY: 'Order is being delivered',
        DELIVERED: 'Order was delivered',
        CANCELLED: 'Order was cancelled by customer',
        DECLINED: 'Order was declined by manager'
    }
