# This is the script based on Dash, plotly version x.x. to build the MAPMAKER
# online application. This application was created using the online manual of
# plotly: https://dash.plotly.com/introduction
# html.Div is used to create single building blocks that can be arranged with
# specific commands to create the layout of the app.

# Author: Dominic Eriksson
# Envrionmental Physics Group
# ETH Zurich
# Switzerland
# dominic.eriksson@usys.ethz.ch

# Date: 20/01/2021

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# cd C:/Users/domin/OneDrive/Documents/MAPMAKER/Python
# cd C:/Users/domin/OneDrive/Documents/MAPMAKER/Final_app
# cd C:/Users/domin/OneDrive/Documents/MAPMAKER/Species_Richness_Analysis
# os.chdir("C:/Users/domin/OneDrive/Documents/MAPMAKER/Species_Richness_Analysis")
# os.chdir("C:/Users/domin/OneDrive/Documents/MAPMAKER/Species_Richness_Analysis/CSV_Files")


## Python codes important:
# df_4 = df[(df["Country Name"] == "Arab World") & (df["Value"] < 1)]    filter data frame in regard to specific values



###=============================================================================
### 1. Preparatory =============================================================
###=============================================================================
# 1.1   Load required libraries
import os
import glob

# Libaries for layout options, layout components, layout structuring
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# Libaries for graph options and interactivity
import plotly.express as px
import plotly.graph_objects as go

# Libaries for data manipulation
import pandas as pd

# Specific style sheet library and input output functions for callbacks
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output



# 1.2 Load the style sheet that you use. The .css file contain several options
# for structuring the app layout such as font sizes, display, etc.
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# 1.3 Initialize the application
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app =  JupyterDash(__name__, external_stylesheets=[dbc.themes.SLATE])
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
app =  dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE, FONT_AWESOME])
server = app.server

# 1.7 Set colors used in the web application
colors = {
    "background": "#272b30", # those numbers encode for so called hex colors. They can easily be googled to find the right numberical encoding for specific colors
    "box": "#3a3f44",
    "text": "#FFFFFF",
    "mapLegend": "#7a8288"
}



test = glob.glob("*.xlsx")
fileNames = glob.glob("*.csv")
# 1.5   Load the data

# this is the coding for the callback part "group_esm_rcp_div"
df_all_data = {
# Diatoms
"Diatom_CNRM_PISCES_RCP26_hsi" : pd.read_csv(fileNames[0]),
"Diatom_CNRM_PISCES_RCP45_hsi" : pd.read_csv(fileNames[1]),
"Diatom_CNRM_PISCES_RCP85_hsi" : pd.read_csv(fileNames[2]),
"Diatom_GFDL_TOPAZ_RCP26_hsi" : pd.read_csv(fileNames[3]),
"Diatom_GFDL_TOPAZ_RCP45_hsi" : pd.read_csv(fileNames[4]),
"Diatom_GFDL_TOPAZ_RCP85_hsi" : pd.read_csv(fileNames[5]),
"Diatom_IPSL_PISCES_RCP26_hsi" : pd.read_csv(fileNames[6]),
"Diatom_IPSL_PISCES_RCP45_hsi" : pd.read_csv(fileNames[7]),
"Diatom_CNRM_PICSES_RCP85_hsi" : pd.read_csv(fileNames[8]),

# Phytoplankton
"Phytoplankton_CNRM_PISCES_RCP26_hsi" : pd.read_csv(fileNames[9]),
"Phytoplankton_CNRM_PISCES_RCP45_hsi" : pd.read_csv(fileNames[10]),
"Phytoplankton_CNRM_PISCES_RCP85_hsi" : pd.read_csv(fileNames[11]),
"Phytoplankton_GFDL_TOPAZ_RCP26_hsi" : pd.read_csv(fileNames[12]),
"Phytoplankton_GFDL_TOPAZ_RCP45_hsi" : pd.read_csv(fileNames[13]),
"Phytoplankton_GFDL_TOPAZ_RCP85_hsi" : pd.read_csv(fileNames[14]),
"Phytoplankton_IPSL_PISCES_RCP26_hsi" : pd.read_csv(fileNames[15]),
"Phytoplankton_IPSL_PISCES_RCP45_hsi" : pd.read_csv(fileNames[16]),
"Phytoplankton_IPSL_PISCES_RCP85_hsi" : pd.read_csv(fileNames[17]),

# Plankton total
"PlanktonTotal_CNRM_PISCES_RCP26_hsi" : pd.read_csv(fileNames[18]),
"PlanktonTotal_CNRM_PISCES_RCP45_hsi" : pd.read_csv(fileNames[19]),
"PlanktonTotal_CNRM_PISCES_RCP85_hsi" : pd.read_csv(fileNames[20]),
"PlanktonTotal_GFDL_TOPAZ_RCP26_hsi" : pd.read_csv(fileNames[21]),
"PlanktonTotal_GFDL_TOPAZ_RCP45_hsi" : pd.read_csv(fileNames[22]),
"PlanktonTotal_GFDL_TOPAZ_RCP85_hsi" : pd.read_csv(fileNames[23]),
"PlanktonTotal_IPSL_PISCES_RCP26_hsi" : pd.read_csv(fileNames[24]),
"PlanktonTotal_IPSL_PISCES_RCP45_hsi" : pd.read_csv(fileNames[25]),
"PlanktonTotal_IPSL_PISCES_RCP85_hsi" : pd.read_csv(fileNames[26]),

# Zooplankton
"Zooplankton_CNRM_PISCES_RCP26_hsi" : pd.read_csv(fileNames[27]),
"Zooplankton_CNRM_PISCES_RCP45_hsi" : pd.read_csv(fileNames[28]),
"Zooplankton_CNRM_PISCES_RCP85_hsi" : pd.read_csv(fileNames[29]),
"Zooplankton_GFDL_TOPAZ_RCP26_hsi" : pd.read_csv(fileNames[30]),
"Zooplankton_GFDL_TOPAZ_RCP45_hsi" : pd.read_csv(fileNames[31]),
"Zooplankton_GFDL_TOPAZ_RCP85_hsi" : pd.read_csv(fileNames[32]),
"Zooplankton_IPSL_PISCES_RCP26_hsi" : pd.read_csv(fileNames[33]),
"Zooplankton_IPSL_PISCES_RCP45_hsi" : pd.read_csv(fileNames[34]),
"Zooplankton_IPSL_PISCES_RCP85_hsi" : pd.read_csv(fileNames[35]),
}


# df_all_data = {"total": df_PlanktonTotal_CNRM_PISCES_RCP26_hsi, "diatoms": df_Diatom_CNRM_PICSES_RCP26_hsi, "zoo": df_Zooplankton_CNRM_PISCES_RCP26_hsi}

## Test data for time series
df_timeSeries = px.data.stocks()
fig = px.area(df_timeSeries, x='date', y="GOOG")
fig.update_layout(paper_bgcolor = colors["box"], font_color = colors["mapLegend"])

# Title
def drawTitle():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H1("Marine Plankton diversity bioindicator scenarios for policy makers, MAPMAKER"),
                ], style = {'textAlign': 'center'})
            ])
        )
    ])

# Project description
def drawProject_description():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H5("Global marine biodiversity supplies essential ecosystems services to human societies."
                            "Marine plankton fuel ocean productivity, drive global biogeochemical cycles and"
                            "regulate the Earth’s climate. Climate-mediated loss of biodiversity has been suggested"
                            "to negatively impact ocean ecosystem services. MAPMAKER is a result between a collaboration"
                            "between IUCN Global Marine and Polar Programme and ETH Environmental Physics Group (UP) to"
                            "inform data-driven decision making on marine biodiversity protection at the international policy"
                            "level. With the financial support of the Geneva Science Policy Interface (GSPI) we used"
                            "observational data and novel machine learning algorithms we mapped 859 marine plankton species"
                            "and define ocean biomes, project future changes in biodiversity and identify hotspots of"
                            "biodiversity changes of total and several planktonic groups. The interactive web tool will"
                            "serve to transfer knowledge across the science-policy-society interface since plankton has"
                            "not yet been incorporated in any global assessment report about the effects of climate"
                            "change on biodiversity and ecosystem services."),
                ], style = {"textAlign": "justify"})
            ])
        )
    ])


###=============================================================================
### 2. Application Layout ======================================================
###=============================================================================
app.layout = dbc.Container([
# Card and CardBody are the main buidling blocks, all layout components are framed within them
    dbc.Card(
        dbc.CardBody([
# Header
            dbc.Row([
                dbc.Col([
                    drawTitle() # we defined the header in the Preparatory section
                ], width = 12),
                ], align = "center"), # end of header

html.Br(), # line break

# RadioItems
        dbc.Card( # Card for all RadioItems
            dbc.CardBody([ # CardBody for all RadioItems

              html.Div([ #ESM radioItem
                dbc.Label("Earth System Models", style = {"font-weight": "bold"}),
                html.I(className="fas fa-question-circle fa-lg", id="info_esm", style = {"font-size": 15, "marginLeft": "10px"}),
                dbc.Tooltip("The three different Earth System Models used "
                "are fully coupled models from the CMIP5 assessment",
                target="info_esm"),
                dbc.RadioItems(
                    options = [
                        {"label": "CNRM-CM5", "value": "CNRM_PISCES",},
                        {"label": "GFDL-ESM2M", "value": "GFDL_TOPAZ"},
                        {"label": "IPSL-CM5A-LR", "value": "IPSL_PISCES"}
                    ],
                    value = "CNRM_PISCES",
                    id = "ESMs"),
              ], style = {"display": "inline-block", "marginLeft": "30px", "verticalAlign": "top"}), # end of ESM radioItem

              html.Div([ # rcp radioItem
                dbc.Label("Representative Concentration Pathway", style = {"font-weight": "bold"}),
                html.I(className = "fas fa-question-circle fa-lg", id = "info_rcp", style = {"font-size": 15, "marginLeft": "10px"}),
                dbc.Tooltip("The Intergovernmental Panel on Climate Change provide policymakers "
                "with scientific assessments on climate change such as the published scenarios of "
                "greenhouse gas concentration and emission pathways called representative "
                "concentration pathways (RCPs). The different climate scenarios are labelled "
                "after their respective radiative forcing in the year 2100 (e.g. RCP8.5 Wm-2). "
                "At present, global carbon emissions are tracking just above the highest "
                "representative concentration pathway (RCP 8.5) while the RCP 2.6 scenario "
                "represents the lowest concentration pathway with high mitigation strategies. ",
                target = "info_rcp"),
                dbc.RadioItems(
                    options = [
                        {"label": "RCP 2.6 (Paris Agreement)", "value": "RCP26"},
                        {"label": "RCP 4.5", "value": "RCP45"},
                        {"label": "RCP 8.5 (Buisness as usual)", "value": "RCP85"}
                    ],
                    value = "RCP26",
                    id = "rcps")
               ], style = {"display": "inline-block", "marginLeft": "30px", "verticalAlign": "top"}), # end of rcp radioItem

               html.Div([ # marine group radioItem
                dbc.Label("Marine Plankton Groups", style = {"font-weight": "bold"}),
                html.I(className = "fas fa-question-circle fa-lg", id = "info_marineGroups", style = {"font-size": 15, "marginLeft": "10px"}),
                dbc.Tooltip("Marine taxonomic groupings important for "
                "global ecosystem services provided by our oceans.",
                target = "info_marineGroups"),
                dbc.RadioItems(
                    options = [
                        {"label": "Total Plankton", "value": "PlanktonTotal"},
                        {"label": "Zooplankton", "value": "Zooplankton"},
                        {"label": "Phytoplankton", "value": "Phytoplankton"},
                        {"label": "Diatoms", "value": "Diatom"}
                    ],
                value = "PlanktonTotal",
                id = "groups")
               ], style = {"display": "inline-block", "marginLeft": "30px", "verticalAlign": "top"}), # end of marine group radioItem

              html.Div([ # diversity radioItem
                dbc.Label("Diversity Indices", style = {"font-weight": "bold"}),
                html.I(className = "fas fa-question-circle fa-lg", id = "info_divIndices", style = {"font-size": 15, "marginLeft": "10px"}),
                dbc.Tooltip("Different diversity indices based on the "
                "Habitat Suitability Index.", target = "info_divIndices"),
                dbc.RadioItems(
                    options = [
                        {"label": "Biomes", "value": "biomes"},
                        {"label": "Shannon Indes", "value": "SI"},
                        {"label": "Hotspots of Diversity Change", "value": "divChange"}
                        ],
                    value = "biomes",
                    id = "bioInd")
              ], style = {"display": "inline-block", "marginLeft": "30px", "verticalAlign": "top"}) # end of diversity radioItem

            ]) # End of radioItem Cardbody
          ), # end of radioItem Card

    html.Br(), # line break

# Insert map component
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id="map-with-slider",
                config = {"scrollZoom": False}) # disble zoom option
            #figure = fig,
            # style = {"width": "100%",  "color": "dark"}
            ], width = 12)
        ]), # enf of graph component

    html.Br(), # line break

# Slider
    dbc.CardBody([
        html.Div([
            dbc.Label("Years", html_for="slider", style = {"font-weight": "bold", "marginLeft": "45%"}),
            dcc.Slider(id="year-slider", min=2012, max=2100, step=1, value=2050,
            marks = {
                2012: {"label": "2012"},
                2020: {"label": "2020"},
                2030: {"label": "2030"},
                2040: {"label": "2040"},
                2050: {"label": "2050"},
                2060: {"label": "2060"},
                2070: {"label": "2070"},
                2080: {"label": "2080"},
                2090: {"label": "2090"},
                2100: {"label": "2100"}
            })
        ])
    ]), # end of slider component

    html.Br(), # line break

# Insert project description
    dbc.Row([
        dbc.Col([
            drawProject_description()
        ], align = "center"),
      ]), # end of project description, was designed in Preparation section

     html.Br(), # line break

#insert time series
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Graph(id = "timeseries-hoover",
                figure = fig,
                style = {"width": "100%", "display": "inline-block",})
            ], style = {"backgroundColor": colors["box"]}),
            dbc.Col([
                dcc.Graph(id = "timeseries-sst",
                figure = fig,
                style = {"width": "100%", "display": "inline-block"})
            ], style = {"backgroundColor": colors["box"]})
        ])
    ]),
    html.Br(),

# Inser Logos and use href to link them to the homepages
    html.Div([
        html.A([
            html.Div(html.Img(src = '/assets/ETH_logo.png', style = {"width": "70px", "height": "40px"}), style = {"display": "inline-block", "marginLeft": "5px"})],
            href = "https://up.ethz.ch/research/ongoing-projects.html"),
        html.A([
            html.Div(html.Img(src = "/assets/GSPI_logo.png", style = {"width": "80px", "height": "40px"}), style = {"display": "inline-block", "marginLeft": "10px"})],
            href = "https://gspi.ch/collaboration_projec/marine-plankton-diversity-bioindicator-scenarios-for-policy-makers-mapmaker/"),
        html.A([
            html.Div(html.Img(src = "/assets/IUCN_logo.png", style = {"width": "40px", "height": "40px"}), style = {"display": "inline-block", "marginLeft": "10px"})],
            href = "https://www.iucn.org/theme/marine-and-polar")
        ]) # end of logos

        ], style = {"backgroundColor": colors["background"]}) # end of general CardBody
    ) # End of Card
]) # End of general Container


###=============================================================================
### 3. App interactivity =======================================================
##=============================================================================
@app.callback(
    Output("map-with-slider", "figure"),
    [Input("groups", "value"),
    Input("ESMs", "value"),
    Input("rcps", "value"),
    Input("year-slider", "value")])
def update_figure(selected_group, selected_esm, selected_rcp, selected_year):
    df = df_all_data[selected_group + "_" + selected_esm + "_" + selected_rcp + "_hsi"]
    df2 = df[["lon", "lat", str(selected_year)]]

    fig = px.scatter_geo(df, lon = "lon", lat = "lat", color = str(selected_year), color_continuous_scale = "Jet")  # color_continuous_scale = "Bluered" to change color scale

    fig.update_geos(projection_type = "natural earth", bgcolor = colors["background"])
    fig.update_layout(height = 400, margin = {"r": 0, "t": 0, "l": 0, "b": 0},
                        paper_bgcolor = colors["background"], transition_duration = 500, font_color = colors["mapLegend"])

    return fig
#
# @app.callback(
#     Output("timeseries-hoover", "figure"),
#     [Input]
# )

if __name__ == '__main__':
    app.run_server(debug=True)
