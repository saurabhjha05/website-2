# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 21:50
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160215_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(help_text='The main, all caps text of the frame.', required=True)), ('tagline', wagtail.wagtailcore.blocks.RichTextBlock(help_text='The smaller, regular cased text under the headline.', template='blocks/strip_rich_text.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='The image serving as the background of the frame. Minimum 1080 pixels wide.', required=True)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('dark', 'Dark'), ('light', 'Light')], icon='cog')), ('call_to_action', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('uri', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('text', wagtail.wagtailcore.blocks.CharBlock(required=True))), classname='call_to_action'), help_text='The large button calling to user toact. Last element receives the most emphasis.')), ('signup_form', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Check to display an email signup form in this frame.', required=False)))), help_text='A horizontal scrolling set of images with text overlaid.', icon='cogs', template='blocks/carousel.html')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), blank=True),
        ),
    ]
