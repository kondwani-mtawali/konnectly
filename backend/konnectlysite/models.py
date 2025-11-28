from django.db import models

# --- AUTO GENERATED FROM dbdiagram.io schema with foreign keys ---
"""
models.py
Automatically generated using script that converts sql-diagram to models script
"""


class Country(models.Model):
    name = models.CharField(max_length=110, blank=True)
    region = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=50, blank=True)
    gross_national_income = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True
    )
    exchange_rate_to_usd = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True
    )
    population = models.BigIntegerField(blank=True)
    labor_force_participation = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True
    )
    population_growth_rate = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True
    )
    gdp = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    gdp_growth_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    merchandise_trade = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    tariff_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    value_of_exports = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    value_of_imports = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    trade_rating = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    fdi_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    political_stability_percentile = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True
    )
    political_context = models.TextField(blank=True)  # Drop down menu
    economic_highlights = models.TextField(blank=True)  # Drop down menu

    def __str__(self):
        return self.name


class Sectors(models.Model):
    country_id = models.ForeignKey("Country", on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    economic_contribution_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True
    )
    growth_trend = models.TextField(blank=True)

    def __str__(self):
        return self.name


class InvestmentPathway(models.Model):
    country_id = models.ForeignKey("Country", on_delete=models.CASCADE)
    investment_pathway_1 = models.TextField(blank=True)
    investment_pathway_2 = models.TextField(blank=True)
    investment_pathway_3 = models.TextField(blank=True)

    def __str__(self):
        return f"{self.country_id.name} - Pathways"
