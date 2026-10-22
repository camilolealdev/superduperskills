---
name: inventory-forecasting
description: "Forecast inventory needs using demand analysis, safety stock calculations, reorder point optimization, and seasonal adjustment"
---

# Inventory Forecasting

## Overview

Master inventory optimization by accurately forecasting demand, calculating optimal stock levels, and reducing carrying costs while avoiding stockouts. Effective forecasting balances supply availability with storage costs.

## Demand Forecasting Methods

### 1. Historical Trending

**Simple Moving Average** (best for stable demand):
```
Month | Actual Demand | 3-Month MA | 6-Month MA
-------|---------------|-----------|----------
Jan | 1,000 | - | -
Feb | 1,100 | - | -
Mar | 950 | 1,017 | -
Apr | 1,200 | 1,083 | -
May | 1,150 | 1,100 | 1,067
Jun | 1,300 | 1,217 | 1,117
Jul | 1,250 | 1,233 | 1,150
Aug | 1,100 | 1,217 | 1,183
Sep | 1,400 | 1,250 | 1,250
Oct | 1,300 | 1,267 | 1,267
Nov | 1,500 | 1,400 | 1,308
Dec | 1,450 | 1,417 | 1,350

Average Annual Demand: 1,250 units/month
Forecast for Jan Year 2: 1,417 (3-month MA)
```

**Weighted Moving Average** (recent data more important):
```
Recent months get higher weights:
- 3 months ago: 20% weight
- 2 months ago: 35% weight
- Last month: 45% weight

Forecast = (Sep × 0.20) + (Oct × 0.35) + (Nov × 0.45)
         = (1,400 × 0.20) + (1,300 × 0.35) + (1,500 × 0.45)
         = 280 + 455 + 675
         = 1,410 units
```

### 2. Seasonal Adjustment

**Identify Seasonality**:
```
Month | Actual | Annual Avg | Seasonal Index
-------|--------|-----------|----------------
Jan | 800 | 1,200 | 0.67 (slower)
Feb | 900 | 1,200 | 0.75
Mar | 1,100 | 1,200 | 0.92
Apr | 1,400 | 1,200 | 1.17 (faster)
May | 1,600 | 1,200 | 1.33 (peak)
Jun | 1,500 | 1,200 | 1.25
Jul | 1,400 | 1,200 | 1.17
Aug | 1,300 | 1,200 | 1.08
Sep | 1,100 | 1,200 | 0.92
Oct | 1,000 | 1,200 | 0.83
Nov | 1,200 | 1,200 | 1.00
Dec | 2,000 | 1,200 | 1.67 (holiday peak)

Average index: 12.07 / 12 = 1.00 (verification)
```

**Seasonal Forecast** (using seasonal index):
```
Base forecast (trend): 1,250 units
Seasonal forecast for May: 1,250 × 1.33 = 1,663 units (peak season)
Seasonal forecast for Jan: 1,250 × 0.67 = 838 units (slow season)
Seasonal forecast for Dec: 1,250 × 1.67 = 2,088 units (holiday)
```

### 3. Regression Analysis

**Linear Trend with Demand Driver**:
```
Regression: Demand = Base + (Growth Rate × Month) + (Seasonal Factor)

Data analysis:
- Base demand: 1,200 units
- Growth rate: +25 units/month (+2% monthly growth)
- Seasonal adjustments: (as above)

Forecast for Month 25 (13 months forward):
= 1,200 + (25 × 25) + (seasonal index for that month)
= 1,200 + 625 + seasonal
= 1,825 + seasonal (if month has 1.1 seasonal index: 1,825 × 1.1 = 2,008 units)
```

### 4. Demand Driver Analysis

**Identify what drives demand**:
```
Demand Driver | Correlation | Lead Time | Action
--------------|-------------|-----------|-------
Marketing spend | 0.85 (strong) | 2 weeks | Forecast up 30% if large campaign planned
Sales pipeline | 0.92 (strong) | 1 month | Request deals closing in next 30 days
Competitor actions | 0.60 (moderate) | 1 month | Monitor competitor price cuts
Seasonal events | 0.75 (strong) | 3 months | Plan for holidays, back-to-school, etc.
Economic indicators | 0.40 (weak) | 2 months | Monitor consumer confidence index
Industry growth | 0.70 (moderate) | Continuous | Factor in industry growth rate

FORECAST ADJUSTMENT:
If large marketing campaign planned in 2 weeks (30% demand lift expected):
- Normal forecast for weeks 3-6: 1,250 units/week
- Adjusted forecast: 1,250 × 1.30 = 1,625 units/week (4-week impact)
```

## Safety Stock Calculation

**Purpose**: Buffer against demand variability and supply delays

**Basic Safety Stock Formula**:
```
Safety Stock = Z × σ_L × √(L)

Where:
Z = Service level factor (95% = 1.65, 99% = 2.33)
σ_L = Standard deviation of demand
L = Lead time in periods

EXAMPLE:
Average monthly demand: 1,250 units
Demand std dev: 150 units (high variability)
Lead time: 2 months
Service level target: 95% (Z = 1.65)

Safety Stock = 1.65 × 150 × √2
             = 1.65 × 150 × 1.41
             = 350 units (safety buffer)
```

**Service Level Trade-offs**:
```
Service Level | Z Factor | Safety Stock | Stockout Risk | Carrying Cost
--------------|----------|--------------|---------------|---------------
90% | 1.28 | 272 units | 10% | Lower
95% | 1.65 | 350 units | 5% | Moderate
99% | 2.33 | 495 units | 1% | Higher
99.9% | 3.09 | 656 units | 0.1% | Very High

TRADE-OFF: 95% service level is typical balance of stockout risk vs. cost
```

## Reorder Point (ROP)

**When to reorder** (balance lead time demand + safety buffer):

```
ROP = (Average Daily Demand × Lead Time) + Safety Stock

EXAMPLE:
Monthly demand: 1,250 units
Daily demand: 1,250 / 30 = 41.67 units/day
Lead time: 14 days (2 weeks from supplier)
Safety stock: 350 units (calculated above)

ROP = (41.67 × 14) + 350
    = 583 + 350
    = 933 units

ACTION: When inventory hits 933 units, place new order
```

**ROP Sensitivity to Lead Time**:
```
Lead Time | Demand During LT | Safety Stock | ROP | Comment
-----------|------------------|--------------|-----|--------
1 week | 292 units | 350 | 642 | Tight; need good forecast
2 weeks | 583 units | 350 | 933 | Standard lead time
4 weeks | 1,167 units | 350 | 1,517 | Long lead; high ROP
8 weeks | 2,333 units | 350 | 2,683 | Very long lead; expensive to carry
```

**Implication**: Shorter lead times allow lower ROP and less inventory carrying cost.

## Economic Order Quantity (EOQ)

**How much to order** (balance order costs vs. carrying costs):

```
EOQ = √(2 × D × S / H)

Where:
D = Annual demand (units)
S = Order cost per order ($)
H = Annual holding cost per unit ($)

EXAMPLE:
Annual demand: 15,000 units (1,250/month × 12)
Order cost: $50 per order (processing, shipping, receiving)
Holding cost: $10 per unit per year (20% of $50 unit cost)

EOQ = √(2 × 15,000 × 50 / 10)
    = √(150,000)
    = 387 units per order

Order frequency: 15,000 / 387 = 39 orders/year (weekly ordering)
Average inventory: 387 / 2 = 194 units (plus safety stock)
```

**EOQ Trade-off Analysis**:
```
Order Quantity | Order Freq | Order Cost/Yr | Carrying Cost/Yr | Total Cost | Note
--------------|-----------|---------------|------------------|-----------|------
100 units | 150 orders | $7,500 | $500 | $8,000 | Too frequent
387 units | 39 orders | $1,950 | $1,935 | $3,885 | OPTIMAL (EOQ)
500 units | 30 orders | $1,500 | $2,500 | $4,000 | Higher carrying
1,000 units | 15 orders | $750 | $5,000 | $5,750 | Bulk discount? Consider if available
```

## Inventory Forecasting Template

**Monthly Forecast Report**:

```
INVENTORY FORECAST - Q2 2024

PRODUCT: Widget Classic

HISTORICAL DEMAND:
January: 1,200 units
February: 1,100 units
March: 1,350 units
Average: 1,217 units/month
Std Dev: 125 units (moderate variability)

FORECAST METHODOLOGY:
- Base: 3-month weighted moving average
- Adjustment: +15% seasonal factor for Q2 (spring season)
- Driver adjustment: +5% for planned marketing campaign in April
- Trend: +2% overall growth

DEMAND FORECAST:
April: 1,400 units (1,217 × 1.15 × 1.05 × 1.02 = 1,405)
May: 1,500 units (peak season)
June: 1,450 units (tail-end seasonal)

INVENTORY PLANNING:
Current stock: 800 units
Safety stock required: 350 units
ROP (reorder point): 933 units

PROCUREMENT PLAN:
April 1: Place order for 1,500 units (EOQ adjusted for demand)
Supplier lead time: 14 days
Expected delivery: April 15 (before peak demand)

INVENTORY PROJECTIONS:
April 1 inventory: 800 units (below ROP; trigger order immediately)
April 15 (delivery): 800 + 1,500 = 2,300 units
April 30 (end month): 2,300 - 1,400 = 900 units
May 31 (end month): 900 + 1,500 - 1,500 = 900 units
June 30: 900 + ? - 1,450 = target 350+ safety stock

RISKS:
- High variability in demand; safety stock may be inadequate
- Supplier lead time 14 days; disruption = 2-week shortage risk
- Marketing campaign success uncertain; demand could exceed 1,405

MITIGATION:
- Increase safety stock to 400 units (add 1 week buffer)
- Dual-source supplier to reduce lead time risk
- Monitor campaign performance weekly; adjust forecast if needed
```

## Seasonal Adjustment Framework

**Build Seasonal Factor Table**:

```
SEASONAL ANALYSIS - Last 3 Years Average

Month | 2021 | 2022 | 2023 | 3-Yr Avg | Annual Avg | Index
-------|------|------|------|----------|-----------|-------
Jan | 800 | 850 | 900 | 850 | 1,200 | 0.71
Feb | 900 | 950 | 1,000 | 950 | 1,200 | 0.79
Mar | 1,100 | 1,150 | 1,200 | 1,150 | 1,200 | 0.96
Apr | 1,400 | 1,450 | 1,500 | 1,450 | 1,200 | 1.21
May | 1,600 | 1,650 | 1,700 | 1,650 | 1,200 | 1.38
Jun | 1,500 | 1,550 | 1,600 | 1,550 | 1,200 | 1.29
Jul | 1,400 | 1,450 | 1,500 | 1,450 | 1,200 | 1.21
Aug | 1,300 | 1,350 | 1,400 | 1,350 | 1,200 | 1.13
Sep | 1,100 | 1,150 | 1,200 | 1,150 | 1,200 | 0.96
Oct | 1,000 | 1,050 | 1,100 | 1,050 | 1,200 | 0.88
Nov | 1,200 | 1,250 | 1,300 | 1,250 | 1,200 | 1.04
Dec | 2,000 | 2,100 | 2,200 | 2,100 | 1,200 | 1.75

Base Annual Average: 14,400 / 12 = 1,200 units/month

SEASONAL PATTERN:
- Weak season: Jan-Mar (index < 1.0)
- Strong season: Apr-Aug (index > 1.0)
- Peak season: May & Dec (holiday/spring)
```

## Forecasting Accuracy Metrics

**Track and Improve Forecast Quality**:

```
Accuracy Metrics:
- MAE (Mean Absolute Error): Average forecast error (units)
- MAPE (Mean Absolute Percentage Error): Error as % of actual
- Bias: Are forecasts consistently high or low?

FORECAST ACCURACY REPORT - Q1 2024:

Month | Forecast | Actual | Error | % Error | Status
-------|-----------|--------|-------|---------|--------
Jan | 1,250 | 1,200 | -50 | -4% | Within 5%
Feb | 1,200 | 1,100 | -100 | -9% | Over-forecast
Mar | 1,350 | 1,350 | 0 | 0% | Accurate
Q1 Average MAPE: 4.3%

IMPROVEMENT ACTIONS:
- Feb forecast too high; analyze why (promotional campaign delayed?)
- Improve demand driver tracking
- Reduce seasonal index adjustment (was 1.15, should be 1.08)
```

## Inventory Optimization Decisions

**Make/Buy Decisions for Carrying Cost**:

```
SCENARIO: Reduce inventory to cut carrying costs

Current State:
- Average inventory: 900 units
- Carrying cost: $10/unit/year = $9,000/year
- Stockout incidents: 2-3/year (due to variability)
- Lost sales: ~$15,000/year (stockout costs)

OPTION 1: Reduce safety stock from 350 to 200 units
- New average inventory: 750 units
- New carrying cost: $7,500/year (save $1,500)
- Expected stockouts: Increase to 5-6/year
- Lost sales: Increase to ~$25,000/year (cost $10,000 more)
- NET IMPACT: LOSE $8,500/year (not recommended)

OPTION 2: Reduce order lead time from 14 to 7 days (faster supplier)
- New ROP: 583 units (down from 933)
- Average inventory: 400 units
- Carrying cost: $4,000/year (save $5,000)
- Stockout risk: Decrease (faster replenishment)
- Supplier cost increase: $3,000/year (for expedited shipping)
- NET IMPACT: SAVE $2,000/year (recommended)

OPTION 3: Implement demand-driven ordering
- Share sales forecast with supplier
- Supplier holds safety stock instead of us
- Our carrying cost: Minimal
- Supplier profit margin: Lower cost alternative
- Supplier cost: Neutral or pass through to us
- NET IMPACT: Evaluate supplier willingness
```

## Best Practices

1. **Review Monthly**: Update forecasts with actual demand data
2. **Collaborative Planning**: Share forecasts with sales/marketing (CPFR)
3. **Scenario Planning**: Plan for optimistic and pessimistic cases
4. **Supplier Communication**: Share forecasts; enable supplier planning
5. **Inventory Audits**: Verify system accuracy; adjust for shrink
6. **Lead Time Monitoring**: Track if supplier meeting 14-day SLA
7. **Demand Sensing**: Monitor market signals early (campaigns, competitors)
8. **Regular Variance Analysis**: Understand forecast errors; improve methodology

---

**Use this skill to**: Optimize inventory levels, reduce carrying costs, prevent stockouts, and improve supply chain efficiency.
