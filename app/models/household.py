from django.db import models
from django.contrib.auth.models import User

from app.models import Province, Commune, Zone, Quartier

class Household(models.Model):
    designation = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.designation
    
    # def save(self, *args, **kwargs):
    #     if not self.id: 
    #         self.created_by = kwargs.pop('request').user
    #     super().save(*args, **kwargs)

    # to make the save method working

    # def my_view(request):
    # if request.method == 'POST':
    #     form = MyForm(request.POST)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.save(request=request)  # Pass the request object to the save() method
    #         # Rest of the view logic
    # else:
    #     form = MyForm()
    
    # context = {
    #     'form': form
    # }
    # return render(request, 'my_template.html', context)