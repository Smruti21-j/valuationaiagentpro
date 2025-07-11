
import numpy as np

def run_valuation_model(df):
    try:
        revenue = df['Revenue'].values[-1]
        growth_rate = 0.1
        discount_rate = 0.12
        years = 5
        cash_flows = [revenue * ((1 + growth_rate) ** i) for i in range(1, years + 1)]
        npv = sum([cf / ((1 + discount_rate) ** i) for i, cf in enumerate(cash_flows, 1)])
        terminal_value = cash_flows[-1] * (1 + growth_rate) / (discount_rate - growth_rate)
        terminal_value_pv = terminal_value / ((1 + discount_rate) ** years)
        total_value = npv + terminal_value_pv
        return {
            "NPV": round(npv, 2),
            "Terminal Value PV": round(terminal_value_pv, 2),
            "Total Valuation": round(total_value, 2)
        }
    except Exception as e:
        return {"error": str(e)}
