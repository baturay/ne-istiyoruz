
from collections import defaultdict
from django import template
from django.template.defaultfilters import stringfilter

from ..utils import order_by_score
from ..views import CommentList


register = template.Library()


@register.simple_tag(takes_context=True)
def order_comments_by_score_for(context, link):
    """
    Preloads threaded comments in the same way Mezzanine initially does,
    but here we order them by score.
    """
    comments = defaultdict(list)
    qs = link.comments.visible().select_related("user", "user__profile")
    for comment in order_by_score(qs, CommentList.score_fields, "submit_date"):
        comments[comment.replied_to_id].append(comment)
    context["all_comments"] = comments
    return ""

@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True
