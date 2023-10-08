import yfinance as yf
import matplotlib.pyplot as plt

#the list of BIST 100 companies 
bist_100_companies = ['KOCA.IS', 'AEFES.IS','AGHOL.IS','AHGAZ.IS','AKBNK.IS','AKCNS.IS','AKFGY.IS','AKFYE.IS','AKSA.IS'
,'AKSEN.IS','ALARK.IS','ALBRK.IS','ALFAS.IS','ARCLK.IS','ASELS.IS','ASTOR.IS','BERA.IS','BIENY.IS','BIMAS.IS','BRMEN.IS','BRSAN.IS',
'BRYAT.IS','BUCIM.IW','CANTE.IS','CCOLA.IS','CIMSA.IS','CMENT.IS','CWENE.IS','DENGE.IS','DOAS.IS','DOHOL.IS','ECILC.IS',
'ECZYT.IS','EGEEN.IS','EKGYO.IS','ENJSA.IS','ENKAI.IS','EREGL.IS','EUPWR.IS','EUREN.IS','FROTO.IS','GARAN.IS','GENIL.IS'
,'GESAN', 'GLYHO', 'GUBRF', 'GWIND', 'HALKB', 'HEKTS', 'IMASM', 'IPEKE', 'ISBIR', 'ISCTR', 'ISDMR', 'ISGYO', 'ISMEN'
, 'ISYAT', 'IZMDC', 'IZINV', 'KARSN', 'KAYSE', 'KCAER', 'KCHOL', 'KENT', 'KLNMA', 'KMPUR', 'KONTR', 'KONYA', 'KORDS'
, 'KOZAA', 'KOZAL', 'KRDMD', 'KZBGY', 'MAVI', 'MGROS', 'MIATK', 'ODAS', 'OTKAR', 'OYAKC', 'PENTA', 'PETKM', 'PGSUS', 
'PSGYO', 'QNBFB', 'QNBFL', 'QUAGR', 'SAHOL', 'SASA', 'SISE', 'SKBNK', 'SMRTG', 'SNGYO', 'SNKRN', 'SOKM', 'TAVHL', 'TBORG'
, 'TCELL', 'THYAO', 'TKFEN', 'TOASO', 'TSKB', 'TTKOM', 'TTRAK', 'TUKAS', 'TUPRS', 'ULKER', 'UTPYA', 'VAKBN', 'VESBE'
, 'VESTL', 'YEOTK', 'YKBNK', 'YYLGD', 'ZOREN']  


# Getting historical data for all BIST 100 companies for different quarters
q1_data = yf.download(bist_100_companies, start='2023-01-01', end='2023-03-31')
q2_data = yf.download(bist_100_companies, start='2023-04-01', end='2023-06-30')
q3_data = yf.download(bist_100_companies, start='2023-07-01', end='2023-09-30')
full_year_data = yf.download(bist_100_companies, start='2023-01-01', end='2023-10-01')

# Function to plot and show the graph
def plot_graph(data, title):
    # Calculate percentage change from the beginning to the end of the period
    percentage_change = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0] * 100

    # Sort companies based on percentage change
    sorted_companies = percentage_change.sort_values(ascending=False)

    # Get the top 10 performing companies
    top_10_companies = sorted_companies.head(10)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.bar(top_10_companies.index, top_10_companies.values)

    # Set labels and title
    plt.xlabel('Company Ticker')
    plt.ylabel('Percentage Change in Stock Price (%)')
    plt.title(title)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Plotting for different quarters
plot_graph(q1_data, 'Top 10 Performing BIST 100 Companies (Q1 2023)')
plot_graph(q2_data, 'Top 10 Performing BIST 100 Companies (Q2 2023)')
plot_graph(q3_data, 'Top 10 Performing BIST 100 Companies (Q3 2023)')
plot_graph(full_year_data,'Top 10 Performing BIST 100 Companies (Jan 2023 - Oct 2023)')