from xml.dom import minidom

import re

from parser_dates_in_lead import *
from components import *


class ParserWikiDate:
    def __init__(self, path):
        self.xmldoc = minidom.parse(path)

    def get_events(self):
        events = []
        for comp in self.xmldoc.getElementsByTagName('Date'):
            events.append(self.__construct_component(comp))
        return events

    def __construct_component(self, component_xml):
        date_to_construct = Date()
        date_to_construct.designation = self.__extract_component_element(component_xml, 'Designation')
        date_to_construct.time_of_day = self.__extract_component_element(component_xml, 'TimeOfDay')
        date_to_construct.day = self.__extract_component_element(component_xml, 'Day')
        date_to_construct.month = self.__extract_component_element(component_xml, 'Month')
        date_to_construct.year = self.__extract_component_element(component_xml, 'Year')
        date_to_construct.century = self.__extract_component_element(component_xml, 'Century')
        date_to_construct.millenium = self.__extract_component_element(component_xml, 'Millenium')
        date_to_construct.in_text = self.__extract_component_in_text(component_xml)
        return Event(date_to_construct, self.__extract_sentence_from_lead(component_xml))

    def __extract_component_attribute(self, component_xml, attr_name):
        return component_xml.attributes[attr_name].value

    def __extract_component_element(self, component_xml, el_name):
        el = component_xml.getElementsByTagName(el_name)
        if len(el) == 0:
            return ""
        return el[0].attributes['val'].value

    def __extract_sentence_from_lead(self, component_xml):
        lead_id_needed = self.__extract_component_attribute(component_xml, 'LeadID')
        leads = self.xmldoc.getElementsByTagName('Lead')

        html_text = ''
        for lead in leads:
            lead_id = self.__extract_component_attribute(lead, 'id')
            if lead_id == lead_id_needed:
                html_text = self.__extract_component_attribute(lead, 'text')
                break
        length = len(html_text)
        res = ''
        pop_s = False
        h = False
        i = -1
        while i < length - 1:
            i += 1
            if html_text[i] == 'h':
                if html_text[i+1] == '>' and h:
                    h = False
            if h:
                continue
            elif not pop_s:
                if html_text[i] == '<':
                    pop_s = True
                    if html_text[i+1] == 'h':
                        h = True
                else:
                    res += html_text[i]
            else:
                if html_text[i] == '>':
                    pop_s = False
        return res

    def __extract_component_in_text(self, component_xml):
        lead_id_needed = self.__extract_component_attribute(component_xml, 'LeadID')
        leads = self.xmldoc.getElementsByTagName('Lead')

        html_text = ''
        for lead in leads:
            lead_id = self.__extract_component_attribute(lead, 'id')
            if lead_id == lead_id_needed:
                html_text = self.__extract_component_attribute(lead, 'text')
                break

        if html_text == '':
            return ''

        html_parser = ParserDateInLead()
        lead_terminals = html_parser.get_terminals(html_text)

        component_terminals = self.__extract_component_attribute(component_xml, 'FieldsInfo')
        component_terminals = component_terminals.split(';')[:-1]

        result = ''
        for term in component_terminals:
            result += lead_terminals[term] + ' '
        return result
