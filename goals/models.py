from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Spending(models.Model):
    item = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.item}: ${self.price}"

class Goal(models.Model):
    '''
                SETTING NEW GOAL   
        1. Set Period
        2. Set Percent
    '''

    # For spender, before adding the authentication app, use user = User.objects.first() in views
    spender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allGoals')
    # needToSpend = nts for brevity
    needToSpend = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    currentSpending = models.ManyToManyField(Spending, blank=True)
    totalSpending = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    checkAmount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    percentGoal = models.DecimalField(max_digits=14, decimal_places=2, default=0) # TODO: limit from 0-100 %
    percentSpendingFromCheck = models.DecimalField(max_digits=14, decimal_places=2, default=0) # initially 0
    ntsDuration = models.CharField(max_length=21, null=True)

    def __str__(self):
        return f"{self.spender}\nNTS: {self.needToSpend}\nCheck Amount: {self.checkAmount}\nPercent Goal: {self.percentGoal}%\nPeriod: {self.ntsDuration}\nTotal Spending: {self.totalSpending}"