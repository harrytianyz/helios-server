"""
Forms for Helios
"""

from django import forms
from django.conf import settings

from .fields import SplitDateTimeField
from .models import Election
from .widgets import SplitSelectDateTimeWidget


class ElectionForm(forms.Form):
  short_name = forms.SlugField(max_length=40, help_text='no spaces, will be part of the URL for your election, e.g. my-club-2010')
  name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':60}), help_text='the pretty name for your election, e.g. My Club 2010 Election') 
  
  description = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={'cols': 70, 'wrap': 'soft'}), required=False)
  election_type = forms.ChoiceField(label="type", choices = Election.ELECTION_TYPES)
  use_voter_aliases = forms.BooleanField(required=False, initial=False, help_text='If selected, voter identities will be replaced with aliases, e.g. "V12", in the ballot tracking center')
  #use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
  randomize_answer_order = forms.BooleanField(required=False, initial=False, help_text='enable this if you want the answers to questions to appear in random order for each voter')
  
  #### DISABLE EMAIL ####
  # private_p = forms.BooleanField(required=False, initial=False, label="Private?", help_text='A private election is only visible to registered voters.')
  private_p = forms.BooleanField(required=False, initial=False, label="Private?", help_text='For security reasons, the private election feature is diabled.', disabled=True)
  
  help_email = forms.CharField(required=False, initial="", label="Help Email Address", help_text='An email address voters should contact if they need help.')
  
  if settings.ALLOW_ELECTION_INFO_URL:
    election_info_url = forms.CharField(required=False, initial="", label="Election Info Download URL", help_text="the URL of a PDF document that contains extra election information, e.g. candidate bios and statements")
  
  # times
  voting_starts_at = SplitDateTimeField(help_text = 'UTC date and time when voting begins',
                                   widget=SplitSelectDateTimeWidget, required=False)
  voting_ends_at = SplitDateTimeField(help_text = 'UTC date and time when voting ends',
                                   widget=SplitSelectDateTimeWidget, required=False)

  #### MODULARITY FEATURES ####
  modularity_text = forms.BooleanField(required=False, initial="", disabled=True, widget=forms.RadioSelect(), label="Verifiabiilty options", 
  help_text= '''You can customize election verifiability by:\n restricting the votes that can be audited by non-adminstrators and whether administrators can audit. 
  These options can be set separately for when the election is open and closed.
  The default options are set to prevent attacks towards ballot secrecy''')
  audit_perm_choices =  (
    ('anyone', 'Anyone'),
    ('themselves', 'Themselves'),
    ('nobody', 'Nobody')
    )
  audit_perm_open = forms.ChoiceField(initial='nobody', label="Audit restriction when open", choices = audit_perm_choices, help_text='When the election is open, whose votes can be audited?')
  audit_perm_close = forms.ChoiceField(initial='anyone', label="Audit restriction when closed", choices = audit_perm_choices, help_text='When the election is closed, whose votes can be audited?')
  admin_perm_open = forms.BooleanField(required=False, initial=False, label="Admin permission when open", help_text='When the election is open, can administrators audit?')
  admin_perm_close = forms.BooleanField(required=False, initial=True, label="Admin permission when closed", help_text='When the election is closed, can administrators audit?') #widget=forms.HiddenInput()
  # if admin_perm_close.has_changed():

  # this overrides any of the above code
  # def __init__(self, *args, **kwargs):
  #     super(ElectionForm, self).__init__(*args, **kwargs)
  #     self.fields['admin_perm_close'] = forms.BooleanField(required=False, initial=True, label="admin_perm_close")

class ElectionTimeExtensionForm(forms.Form):
  voting_extended_until = SplitDateTimeField(help_text = 'UTC date and time voting extended to',
                                   widget=SplitSelectDateTimeWidget, required=False)
  
class EmailVotersForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=4000, widget=forms.Textarea)
  send_to = forms.ChoiceField(label="Send To", initial="all", choices= [('all', 'all voters'), ('voted', 'voters who have cast a ballot'), ('not-voted', 'voters who have not yet cast a ballot')])

class TallyNotificationEmailForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
  send_to = forms.ChoiceField(label="Send To", choices= [('all', 'all voters'), ('voted', 'only voters who cast a ballot'), ('none', 'no one -- are you sure about this?')])

class VoterPasswordForm(forms.Form):
  voter_id = forms.CharField(max_length=50, label="Voter ID")
  password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

