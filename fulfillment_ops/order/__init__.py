from django.utils.translation import pgettext_lazy


class OrderStatus:
    CREATED = "unfulfilled"
    PARTIALLY_FULFILLED = "partially fulfilled"
    FULFILLED = "fulfilled"
    CANCELED = "canceled"

    CHOICES = [
        (
            UNFULFILLED,
            pgettext_lazy(
                "Status for an order with no items marked as fulfilled", "Unfulfilled"
            ),
        ),
        (
            PARTIALLY_FULFILLED,
            pgettext_lazy(
                "Status for an order with some items marked as fulfilled",
                "Partially fulfilled",
            ),
        ),
        (
            FULFILLED,
            pgettext_lazy(
                "Status for an order with all items marked as fulfilled", "Fulfilled"
            ),
        ),
        (
            CANCELED,
            pgettext_lazy("Status for a permanently canceled order", "Canceled"),
        ),
    ]


class OrderEvents:
    ORDER_CREATED = "created"
    ORDER_ASSIGNED = "assigned"
    ORDER_FULFILLED = "fulfilled"
    ORDER_CANCELED = "canceled"

    CHOICES = [
        (
            ORDER_CREATED,
            pgettext_lazy(
                "Event for created order", "Created"
            ),
        ),
        (
            ORDER_ASSIGNED,
            pgettext_lazy(
                "Event for assigned order", "Assigned"
            ),
        ),
        (
            ORDER_CANCELED,
            pgettext_lazy(
                "Event for cancelled order", "Canceled"
            ),
        ),
        (
            ORDER_FULFILLED,
            pgettext_lazy(
                "Event for fulfilled order", "Fulfilled"
            ),
        ),
    ]
