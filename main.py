# from flask import Flask, render_template, request
# from pycoingecko import CoinGeckoAPI
# import datetime

# cg = CoinGeckoAPI()
# app = Flask(__name__)
# list_cryptocurrencies = cg.get_coins_list()


# @app.route("/")
# def home():
#     return "Hello, World!"


# @app.route("/<cryptocurrency>", methods=("GET", "POST"))
# def dashboard(cryptocurrency):

#     if request.method == "POST" and request.form.get("cryptocurrencies") != "None":
#         cryptocurrency = request.form.get("cryptocurrencies")

#     assets = cg.get_coin_market_chart_by_id(
#         id=cryptocurrency, vs_currency="eur", days="2"
#     )

#     print("*****************************************************")
#     print(assets["prices"])
#     print("*****************************************************")
#     # list_historics = [[nested[0], round(nested[1],4)] for nested in assets['prices']]
#     # print(list(zip(list_historics)))
#     data_historics = [[ass,round(er,3)] for ass,er in assets["prices"]]
#     print(data_historics)
#     print("*****************************************************")


#     unzipped_object = list(zip(*data_historics))

#     return render_template(
#         "main.html",
#         title=cryptocurrency.upper(),
#         max=max(unzipped_object[1]),
#         assets=assets,
#         last=[
#             datetime.datetime.fromtimestamp(point_date / 1000).strftime(
#                 "%Y-%m-%d %H:%M:%S"
#             )
#             for point_date in unzipped_object[0]
#         ],
#         last2=unzipped_object[1],
#     )


# if __name__ == "__main__":
#     app.run(debug=True)
