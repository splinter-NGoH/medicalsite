from .models import CustomerRequests
from django import forms

class CustomerRequestsForm(forms.ModelForm):
    class Meta:
        model= CustomerRequests
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CustomerRequestsForm, self).__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs["class"] = "form-control"
        self.fields["full_name"].widget.attrs["placeholder"] = "Full Name"
        self.fields["phone_number"].widget.attrs["class"] = "form-control"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Phone Number"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["note"].widget.attrs["class"] = "form-control"
        self.fields["note"].widget.attrs["placeholder"] = "Note ملحوظه"