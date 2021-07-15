from  django import forms


from .models import Group


class GroupCreationForm (forms.ModelForm):
    def __init__(self,*args, **kwargs):
        self.admin = kwargs.pop('admin',None)
        super(GroupCreationForm,self).__init__(*args,**kwargs)


    def save(self,force_insert=False,force_update=False,commit=True):
        obj = super(GroupCreationForm,self).save(commit=False)
        obj.admin = self.admin
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Group
        fields = ['name','describe']

    