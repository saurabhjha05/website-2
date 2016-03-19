# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 21:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20160319_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(help_text='The main, all caps text of the frame.', required=True)), ('taglines', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(help_text='The smaller, regular cased text under the headline.'))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='The image serving as the background of the frame. Minimum 1080 pixels wide.', required=True)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('dark', 'Dark'), ('light', 'Light')], icon='cog')), ('call_to_action', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('uri', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('icon', wagtail.wagtailcore.blocks.CharBlock(required=False)))), help_text='Large button to direct user to specific content. Last element has greatest emphasis.', required=False)), ('signup_form', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Check to display an email signup form in this frame.', required=False)))), help_text='A horizontal scrolling set of images with text overlaid.', icon='cogs', template='blocks/carousel.html')), ('team_carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('qualifications', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('uri', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('icon', wagtail.wagtailcore.blocks.CharBlock(required=False)))), required=False)))), icon='group', templates='blocks/team_carousel.html')), ('content_row', wagtail.wagtailcore.blocks.StreamBlock((('promo_paragraph', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2', '2 columns'), ('3', '3 columns'), ('4', '4 columns'), ('5', '5 columns'), ('6', '6 columns'), ('7', '7 columns'), ('8', '8 columns'), ('9', '9 columns'), ('10', '10 columns'), ('11', '11 columns'), ('12', '12 columns')], help_text='Length in Bootstrap columns for display on desktop.')), ('offset', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2', '2 columns'), ('3', '3 columns'), ('4', '4 columns'), ('5', '5 columns'), ('6', '6 columns'), ('7', '7 columns'), ('8', '8 columns'), ('9', '9 columns'), ('10', '10 columns'), ('11', '11 columns'), ('12', '12 columns')], help_text='Offset in Bootstrap columns for display on desktop.', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('text-left', 'Left aligned text'), ('text-center', 'Center aligned text'), ('text-right', 'Right aligned text'), ('text-justify', 'Justified text'), ('text-nowrap', 'No wrap text')], help_text='Alignment for text in content block.', required=False)), ('body', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('call_to_action', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('uri', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('icon', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('button_icon', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('black', 'Black'), ('white', 'White')])), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('lg', 'Large'), ('md', 'Medium'), ('sm', 'Small'), ('xs', 'Extra Small')])))))), ('spacer', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('15', '15 pixels'), ('30', '30 pixels'), ('45', '45 pixels'), ('60', '60 pixels'), ('75', '75 pixels'), ('90', '90 pixels')], required=False)))))))), ('skillbar', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2', '2 columns'), ('3', '3 columns'), ('4', '4 columns'), ('5', '5 columns'), ('6', '6 columns'), ('7', '7 columns'), ('8', '8 columns'), ('9', '9 columns'), ('10', '10 columns'), ('11', '11 columns'), ('12', '12 columns')], help_text='Length in Bootstrap columns for display on desktop.')), ('offset', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2', '2 columns'), ('3', '3 columns'), ('4', '4 columns'), ('5', '5 columns'), ('6', '6 columns'), ('7', '7 columns'), ('8', '8 columns'), ('9', '9 columns'), ('10', '10 columns'), ('11', '11 columns'), ('12', '12 columns')], help_text='Offset in Bootstrap columns for display on desktop.', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('text-left', 'Left aligned text'), ('text-center', 'Center aligned text'), ('text-right', 'Right aligned text'), ('text-justify', 'Justified text'), ('text-nowrap', 'No wrap text')], help_text='Alignment for text in content block.', required=False)), ('skills', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('skill_percentage', wagtail.wagtailcore.blocks.CharBlock()), ('skill_name', wagtail.wagtailcore.blocks.CharBlock())))))))), ('icon_blurb', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2', '2 columns'), ('3', '3 columns'), ('4', '4 columns'), ('5', '5 columns'), ('6', '6 columns'), ('7', '7 columns'), ('8', '8 columns'), ('9', '9 columns'), ('10', '10 columns'), ('11', '11 columns'), ('12', '12 columns')], help_text='Length in Bootstrap columns for display on desktop.')), ('offset', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2', '2 columns'), ('3', '3 columns'), ('4', '4 columns'), ('5', '5 columns'), ('6', '6 columns'), ('7', '7 columns'), ('8', '8 columns'), ('9', '9 columns'), ('10', '10 columns'), ('11', '11 columns'), ('12', '12 columns')], help_text='Offset in Bootstrap columns for display on desktop.', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('text-left', 'Left aligned text'), ('text-center', 'Center aligned text'), ('text-right', 'Right aligned text'), ('text-justify', 'Justified text'), ('text-nowrap', 'No wrap text')], help_text='Alignment for text in content block.', required=False)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Text block passed as the icon selected. Choose between Ionic Icons or FontAwesome.')), ('headline', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('body', wagtail.wagtailcore.blocks.RichTextBlock(required=False))))), ('definition_list', wagtail.wagtailcore.blocks.StructBlock((('width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2', '2 columns'), ('3', '3 columns'), ('4', '4 columns'), ('5', '5 columns'), ('6', '6 columns'), ('7', '7 columns'), ('8', '8 columns'), ('9', '9 columns'), ('10', '10 columns'), ('11', '11 columns'), ('12', '12 columns')], help_text='Length in Bootstrap columns for display on desktop.')), ('offset', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2', '2 columns'), ('3', '3 columns'), ('4', '4 columns'), ('5', '5 columns'), ('6', '6 columns'), ('7', '7 columns'), ('8', '8 columns'), ('9', '9 columns'), ('10', '10 columns'), ('11', '11 columns'), ('12', '12 columns')], help_text='Offset in Bootstrap columns for display on desktop.', required=False)), ('align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('text-left', 'Left aligned text'), ('text-center', 'Center aligned text'), ('text-right', 'Right aligned text'), ('text-justify', 'Justified text'), ('text-nowrap', 'No wrap text')], help_text='Alignment for text in content block.', required=False)), ('definitions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('definition', wagtail.wagtailcore.blocks.CharBlock()))))))))))), ('quotations', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='The image serving as the background of the quotations. Minimum 1080 pixels wide.', required=True)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark')])), ('quotations', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('quotation', wagtail.wagtailcore.blocks.CharBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False))))))))), ('stats', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='The image serving as the background of the quotations. Minimum 1080 pixels wide.', required=True)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark')])), ('stats', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('label', wagtail.wagtailcore.blocks.CharBlock()), ('count', wagtail.wagtailcore.blocks.CharBlock())))))))), ('short_hero', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='The image serving as the header image for the page. Shorter than the carousel, intended for sub pages.', required=True)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark')])), ('title', wagtail.wagtailcore.blocks.CharBlock()), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('statement', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('subtitles', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), required=False)), ('call_to_action', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('uri', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('icon', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('button_icon', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('black', 'Black'), ('white', 'White')])), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('lg', 'Large'), ('md', 'Medium'), ('sm', 'Small'), ('xs', 'Extra Small')])))), help_text='Large button to direct user to specific content. Last element has greatest emphasis.', required=False)), ('signup_form', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Check to display an email signup form in this frame.', required=False)), ('caveats', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), required=False))))), ('soundcloud', wagtail.wagtailcore.blocks.StructBlock((('track_id', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('playlist_id', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('auto_play', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('hide_related', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('show_comments', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('show_user', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('show_reposts', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('visual', wagtail.wagtailcore.blocks.BooleanBlock(required=False)))))), blank=True),
        ),
    ]
