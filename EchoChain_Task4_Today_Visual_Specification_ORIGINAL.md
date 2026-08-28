# EchoChain Project 3 – Task 4
## Power BI Dashboard Visual Specification

**Purpose:** Define the practical visual specification for the EchoChain Power BI dashboard so the implementation can be built consistently from the Task 4 layout plan.

### 1. Dashboard objective
The dashboard should provide an analytical view of EchoChain operations, with emphasis on inventory/shipments, secondary-market activity, product/component information, shelf-life or age-related indicators, and temperature-related observations where those fields are available.

### 2. Recommended report pages

| Page | Purpose | Main visuals |
|---|---|---|
| Executive Overview | High-level operational summary | KPI cards, trend chart, category comparison, status breakdown |
| Market & Shipment Analysis | Analyse market/listing and shipment behaviour | Trend chart, location/category comparison, table |
| Product & Circularity | Examine product/component and circularity indicators | KPI cards, component/product comparison, detail table |
| Data Quality / Details | Validate underlying records and exceptions | Record table, missing-value indicators, exception counts |

### 3. Executive Overview layout
**Top row – KPI cards**
- Total Records
- Total Shipments
- Average Price
- Average Temperature
- Average Remaining Shelf Life (if available)

**Middle row**
- Line chart: Records/shipments over time
- Clustered column chart: Volume by product/category

**Bottom row**
- Donut or stacked column: Status/category distribution
- Detail table: Date, product/category, location, price, temperature, shelf-life indicator

**Slicers**
- Date
- Product/category
- Location
- Status
- Source/market type, if available

### 4. Market & Shipment Analysis
**KPIs**
- Total listings/records
- Average listing/market price
- Shipment count
- Average shipment quantity, if available

**Visuals**
- Line chart: Price or volume trend by date
- Bar chart: Records by location
- Column chart: Records by product/category
- Table: Product, location, date, price, quantity and relevant status fields

### 5. Product & Circularity
**KPIs**
- Number of products/components
- Average remaining shelf life, if available
- Products/components requiring attention
- Circularity-related record count, if available

**Visuals**
- Bar chart: Product/component distribution
- Column chart: Average shelf life by product/category
- Scatter chart: Temperature vs shelf life when both fields exist
- Detail table for product/component records

### 6. Data Quality / Details
Use this page for validation rather than decorative reporting.

Include:
- Record-level table
- Missing-value count
- Duplicate/exception count where validated
- Data source/category
- Last refresh information
- Filters for date, product/category and location

### 7. KPI definitions

| KPI | Definition | Suggested aggregation |
|---|---|---|
| Total Records | Number of records available in the selected filter context | COUNTROWS |
| Total Shipments | Number of shipment records or shipment IDs, depending on the model | COUNT / DISTINCTCOUNT |
| Average Price | Mean price for records in the current filter context | AVERAGE |
| Average Temperature | Mean recorded temperature | AVERAGE |
| Remaining Shelf Life | Remaining usable life derived from the project's agreed shelf-life logic | AVERAGE / appropriate measure |
| Product/Component Count | Distinct products/components in the selected context | DISTINCTCOUNT |

**Important:** Do not invent business values. Map each KPI to the final Gold/Mart model field and use the project's approved calculation logic.

### 8. Visual interaction plan
- Date slicer should affect all analytical pages.
- Product/category slicer should affect all visuals that use product/category.
- Location slicer should affect shipment and market visuals.
- Selecting a bar/line point should cross-filter related visuals.
- Use drill-through only where a detailed record view is required.
- Avoid excessive slicers; keep the main page readable.

### 9. Formatting and usability notes
- Keep page titles consistent.
- Use the same number formatting for the same KPI across pages.
- Use tooltips for additional context rather than overcrowding the canvas.
- Keep tables to decision-useful columns.
- Prefer readable labels and units.
- Keep visual hierarchy: KPIs → trends/comparisons → detailed records.
- Do not use a visual unless it answers a defined business question.

### 10. Field mapping checklist
Before building each visual, confirm:
1. Source table/model
2. Dimension field
3. Measure/value field
4. Date field, if applicable
5. Aggregation rule
6. Filter context
7. Expected business interpretation

### 11. Task 4 contribution
This artifact represents the dashboard-planning contribution for EchoChain Task 4. It converts the dashboard concept into an implementation-ready visual specification that can be followed while building the Power BI report.

### 12. Next implementation step
Connect Power BI to the approved Databricks/Silver/Gold or final analytical model, verify field names and data types, then build the Executive Overview page according to this specification.
