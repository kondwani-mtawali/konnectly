from django.db import models

# --- AUTO GENERATED FROM dbdiagram.io schema with foreign keys ---
"""
models.py
Automatically generated using script that converts sql-diagram to models script
"""


class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=100, blank=True, null=True)
    gross_national_income = models.FloatField(blank=True, null=True)
    exchange_rate_to_usd = models.FloatField(blank=True, null=True)
    population = models.FloatField(blank=True, null=True)
    labor_force_participation = models.FloatField(blank=True, null=True)
    population_growth_rate = models.FloatField(blank=True, null=True)
    gdp = models.FloatField(blank=True, null=True)
    gdp_growth_rate = models.FloatField(blank=True, null=True)
    merchandise_trade = models.FloatField(blank=True, null=True)
    tariff_rate = models.FloatField(blank=True, null=True)
    value_of_exports = models.FloatField(blank=True, null=True)
    value_of_imports = models.FloatField(blank=True, null=True)
    trade_rating = models.FloatField(blank=True, null=True)
    fdi_percentage = models.FloatField(blank=True, null=True)
    political_stability_percentile = models.FloatField(blank=True, null=True)
    political_context = models.TextField(blank=True, null=True)  # Drop down menu
    economic_highlights = models.TextField(blank=True, null=True)  # Drop down menu

    def __str__(self):
        return self.name
