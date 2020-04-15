from django.utils.translation import gettext as _
from djchoices import ChoiceItem, DjangoChoices


class RatingChoices(DjangoChoices):
    G = ChoiceItem("G", label=_("G"))
    PG = ChoiceItem("PG", label=_("PG"))
    PG_13 = ChoiceItem("PG-13", label=_("PG-13"))
    R = ChoiceItem("R", label=_("R"))
    NC_17 = ChoiceItem("NC-17", label=_("NC-17"))
