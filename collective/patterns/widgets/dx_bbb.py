# -*- coding: utf-8 -*-
from plone.app.dexterity.behaviors.metadata import ICategorization
from plone.app.dexterity.behaviors.metadata import IOwnership
from plone.app.dexterity.behaviors.metadata import IPublication
from collective.patterns.widgets.dx import AjaxSelectWidget
from collective.patterns.widgets.dx import DatetimeWidget
from collective.patterns.widgets.dx import QueryStringWidget
from collective.patterns.widgets.dx import RelatedItemsWidget
from collective.patterns.widgets.dx import RichTextWidget
from collective.patterns.widgets.dx import SelectWidget
from collective.patterns.widgets.interfaces import IWidgetsLayer
from collective.patterns.widgets.utils import first_weekday
from z3c.form.interfaces import IFieldWidget
from z3c.form.util import getSpecification
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer

try:
    from plone.app.relationfield.behavior import IRelatedItems
    HAS_RF = True
except ImportError:
    HAS_RF = False

try:
    from plone.app.contenttypes.behaviors.collection import ICollection
    from plone.app.contenttypes.behaviors.richtext import IRichText
    HAS_PAC = True
except ImportError:
    HAS_PAC = False


@adapter(getSpecification(ICategorization['subjects']), IWidgetsLayer)
@implementer(IFieldWidget)
def SubjectsFieldWidget(field, request):
    widget = FieldWidget(field, AjaxSelectWidget(request))
    widget.vocabulary = 'plone.app.vocabularies.Keywords'
    return widget


@adapter(getSpecification(ICategorization['language']), IWidgetsLayer)
@implementer(IFieldWidget)
def LanguageFieldWidget(field, request):
    widget = FieldWidget(field, SelectWidget(request))
    return widget


@adapter(getSpecification(IPublication['effective']), IWidgetsLayer)
@implementer(IFieldWidget)
def EffectiveDateFieldWidget(field, request):
    widget = FieldWidget(field, DatetimeWidget(request))
    widget.pattern_options.setdefault('date', {})
    widget.pattern_options['date']['firstDay'] = first_weekday()
    return widget


@adapter(getSpecification(IPublication['expires']), IWidgetsLayer)
@implementer(IFieldWidget)
def ExpirationDateFieldWidget(field, request):
    widget = FieldWidget(field, DatetimeWidget(request))
    widget.pattern_options.setdefault('date', {})
    widget.pattern_options['date']['firstDay'] = first_weekday()
    return widget


@adapter(getSpecification(IOwnership['contributors']), IWidgetsLayer)
@implementer(IFieldWidget)
def ContributorsFieldWidget(field, request):
    widget = FieldWidget(field, AjaxSelectWidget(request))
    widget.vocabulary = 'plone.app.vocabularies.Users'
    return widget


@adapter(getSpecification(IOwnership['creators']), IWidgetsLayer)
@implementer(IFieldWidget)
def CreatorsFieldWidget(field, request):
    widget = FieldWidget(field, AjaxSelectWidget(request))
    widget.vocabulary = 'plone.app.vocabularies.Users'
    return widget


if HAS_RF:
    @adapter(getSpecification(IRelatedItems['relatedItems']), IWidgetsLayer)
    @implementer(IFieldWidget)
    def RelatedItemsFieldWidget(field, request):
        widget = FieldWidget(field, RelatedItemsWidget(request))
        widget.vocabulary = 'plone.app.vocabularies.Catalog'
        return widget

if HAS_PAC:
    @adapter(getSpecification(ICollection['query']), IWidgetsLayer)
    @implementer(IFieldWidget)
    def QueryStringFieldWidget(field, request):
        return FieldWidget(field, QueryStringWidget(request))

    @adapter(getSpecification(IRichText['text']), IWidgetsLayer)
    @implementer(IFieldWidget)
    def RichTextFieldWidget(field, request):
        return FieldWidget(field, RichTextWidget(request))
