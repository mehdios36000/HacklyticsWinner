import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
from pandas import DataFrame
from rich import print
from typing import List
import openai


FOODS = [
    f.strip()
    for f in "agave nectar,alcohol,alfalfa,almond butter,almond milk,almonds,american cheese,anchovies,apple,apple cider,apple juice,apple pie,applesauce,apricots,artic char,artichokes,arugula,asparagus,avocado,baby carrots,bacon,bagels,baked beans,baked potatoes,balsamic vinegar,banana,banana with peel,barbecue sauce,barley,basil,bean sprouts,bean(seed),beef,beer,beets,bell peppers,berries,biscuits,bison,black beans,blackberries,blue cheese,blueberries,blueberry pie,bok choy,bologna,brazil nuts,bread,bread crumbs,breadsticks,brie cheese,brisket,broccoli,broth,brown rice,brown sugar,brownies,brussels sprouts,bulgur,buns,burgers,burritos,butter,buttermilk,cabbage,caesar dressing,caesar salad,cakes,calamari,calzones,camembert cheese,candies,cantaloupe,capers,cappuccino,carp,carrot,carrot cake,cashews,catfish,cauliflower,celery,celery root,cereal,cereal bars,challah,champagne,chard,chayote squash,cheddar cheese,cheese,cheese pizza,cheeseburgers,cheesecake,cherries,cherry pie,cherry tomatoes,chestnuts,chia seeds,chicken,chicken apple sausage,chicken breast,chicken drumsticks,chicken nuggets,chicken salad,chicken soup,chicken thighs,chicken wings,chickpeas,chilaquiles,chili,chimichangas,chips,chive,chocolate,chocolate cake,chocolate chip cookies,chocolate milk,chow mein,chowders,chutney,cilantro,clams,cobbler,cocoa,coconut milk,coconuts,cod,coffee,coffee creamer,colby cheese,coleslaw,collards,cookies,corn,corn chips,corn dogs,corn nuts,corn on the cob,corn starch,cornbread,corned beef,cornmeal,cottage cheese,country rice,couscous,crab,crackers,cranberries,cranberry juice,crawfish,cream,cream cheese,crepes,crispbread,croissants,croutons,cucumbers,cupcakes,curries,custard,dark chocolate,dates,donuts,duck,dumplings,edamame,eel,egg rolls,egg salad,egg whites,egg yolks,eggnog,eggplant,eggs,empanadas,enchiladas,endive,energy drinks,english muffins,fajitas,falafel,fennel,feta cheese,figs,fish,fish oil,flatbread,flounder,flour,focaccia,french dressing,french fries,french toast,fried chicken,fried eggs,fried rice,fritters,frostings,frozen yogurt,fruit cocktail,fruit punch,fruit salad,fudge,garden salad,garlic,garlic bread,gelatin,ginger,gnocchi,goat cheese,gorgonzola cheese,gouda cheese,goulash,granola,granola bars,grape juice,grapefruit juice,grapefruits,grapes,gravy,greek salad,greek yogurt,green beans,green onions,green peas,grilled chicken,grits,ground beef,ground chicken,ground pork,ground turkey,guacamole,gumbo,gyros,haddock,half and half,halibut,ham,hamburgers,hard boiled eggs,hard cider,hash browns,havarti cheese,herring,hominy,honey,honeydew melons,horseradish,hot chocolate,hot dogs,hummus,ice cream cones,ice cream soda,ice creams,ice pop,iced tea,india pale ale beer,italian dressing,jalapenos,jambalaya,jams,jerky,jicama,kale,ketchup,kidney beans,kimchi,kiwi,lager,lamb,lamb chops,lasagna,latte,leeks,lemon,lemon juice,lemonade,lentils,lettuce,licorice,light beer,lima beans,lime,lo mein,lobster,macadamia nuts,macaroni,macaroni and cheese,mackerel,mahi mahi,mandarin oranges,mangos,maple syrup,margarine,margarita,marshmallows,mashed potatoes,mayonnaise,meatballs,meatloaf,mexican cheese,milk,milk shakes,millet,miso soup,mixed greens,mixed nuts,mixed vegetables,mousse,mozzarella cheese,muenster cheese,muesli,muffins,multigrain bread,mushroom,mussels,mustard,mustard greens,naan,nachos,nectar,nectarines,noodles,nopales,nougat,nut cheese,nutrition bars,nuts,oatmeal,oats,octopus,oil,okra,olive oil,olives,omelets,onion rings,onions,orange,orange juice,orange with peel,oregano,orzo,oysters,paella,pancakes,papayas,parmesan cheese,parsley,parsnips,pasta,pasta salad,pasta sauce,pastrami,pastries,pate nutrition,peach,peaches,peanut butter,peanuts,pears,peas,pecan pie,pecans,pepper,pepperoni,pepperoni pizza,pesto,pickles,pie crust,pies,pilaf,pine nuts,pineapple,pinto beans,pistachios,pita bread,pizza,pizza dough,pizza sauce,plate only,plums,poached eggs,polenta,pomegranate,popcorn,pork,pork chops,pot pies,potato bread,potato chips,potato salad,potato skins,potatoes,pretzels,protein powder,provolone cheese,prunes,puddings,pumpkin seeds,pumpkins,quesadillas,quiche,quinoa,radishes,raisin bran,raisin bread,raisins,ranch dressing,raspberries,ravioli,red potatoes,refried beans,relish,ribs,rice,rice cakes,rice noodles,risotto,roast beef,roast chicken,roast pork,roast turkey,roasted potatoes,rolls,romano cheese,root beer,rosemary,rum,rye bread,salad dressing,salads,salami,salmon,salsa,salt,samosas,sandwich cookies,sandwiches,sardines,sauerkraut,sausage,scallops,scones,scrambled eggs,seafood,seaweed,seeds,shallots,sherbet,shrimp,skim milk,smoked salmon,smoothies,snapper,snow peas,soft serve ice creams,sorbet,souffle,sour cream,sourdough bread,soy milk,soy nuts,soy sauce,soy sausage,soy yogurt,spaghetti,spinach (cooked),spinach (raw),spreads,spring rolls,squash,squid,steak,stews,stout beer,strawberries,string cheese,strudels,stuffing,succotash,sugar,sun dried tomatoes,sundaes,sunflower seeds,sushi,sweet potato,sweet rolls,swiss cheese,swordfish,syrup,tabouli,taco salad,taco shells,tacos,tahini,tamales,taquitos,tatsoi,tea,tempeh,tempura,teriyaki sauce,thyme,tilapia,toast,tofu,tomatillo,tomato soup,tomatoes,tortellini,tortilla,tortilla chips,tostadas,trail mix,trout,tuna,tuna salad,turkey,turkey bacon,turkey breast,turnips,turnover,veal,vegetable juice,vegetable oil,veggie burgers,vinaigrette,vinegar,vodka,wafers,waffles,walnuts,water,water chestnuts,watermelon,wheat beer,wheat berry,wheat bread,white beans,white bread,white rice,white wine,whole wheat bread,wild rice,wine,wraps,yam,yogurt,zucchini".strip().split(
        ","
    )
]

NUTRIENTS = "cal/g,fat(g),carb(g),protein(g),vit_a,vit_c,iron,trans_fat,sat_fat,cholesterol,sodium,carbs,fiber,sugars,calcium,protein,energy".strip().split(
    ","
)

NUTRIENTS_POSITION = {nut: pos for (pos, nut) in enumerate(NUTRIENTS)}


def read_disease_and_serve(fname: str, disease: str):
    df = pd.read_csv(fname)
    return serve(df, disease)


def serve(df: DataFrame, disease: str):
    disease = disease.lower()
    df["Disease"] = df["Disease"].map(lambda s: s.lower())

    matched_rows = str(df[df["Disease"] == disease].to_records()[0][2])
    return [s.strip() for s in matched_rows.split(",")]

def nut_norm_onehot(components: List[str]):
    array = np.zeros([len(NUTRIENTS)])

    for c in components:
        c = c.strip().lower()
        assert c in NUTRIENTS, [c, NUTRIENTS]
        array[NUTRIENTS_POSITION[c]] = np.sqrt(len(components))

    return array


def read_file_and_match(ingredient_food: str, cleaned_recipe: str, nutrients, nono=()):
    nutrients = [n.lower() for n in nutrients]

    if_df = pd.read_csv(ingredient_food)
    cr_df = pd.read_csv(cleaned_recipe)

    return match_ingredients_and_recipe(if_df, cr_df, nutrients, nono)


def match_ingredients_and_recipe(if_df: DataFrame, cr_df: DataFrame, nutrients, nono):
    vector = nut_norm_onehot(nutrients)

    if_df = if_df.loc[:, ["Ingredient"] + NUTRIENTS]
    cr_df = cr_df.loc[:, ["Title", "Instructions"] + FOODS]

    cr_df.dropna(inplace=True)

    if nono:
        for no in nono:
            no = no.lower()
            cr_df = cr_df[~cr_df["Title"].str.lower().str.contains(no)]
            cr_df = cr_df[~cr_df["Instructions"].str.lower().str.contains(no)]

    if_df_mat = (
        if_df.loc[:, NUTRIENTS].to_numpy().astype("float") + np.random.randn() / 1e4
    )
    if_df_mat /= np.linalg.norm(if_df_mat, axis=-1, keepdims=True) + 1e-8

    cr_df_mat = cr_df.loc[:, FOODS].to_numpy().astype("float") + np.random.randn() / 1e4
    cr_df_mat /= np.linalg.norm(cr_df_mat, axis=-1, keepdims=True) + 1e-8

    match_mat = np.einsum("in,ri->rn", if_df_mat, cr_df_mat)
    match_score = np.einsum("rn,n->r", match_mat, vector)
    argsort = np.argsort(match_score)[::-1]

    argsort = argsort[:10]

    titles = cr_df["Title"][argsort]
    instructions = cr_df["Instructions"][argsort]
    scores = match_score[argsort]
    assert len(titles) == len(instructions) == len(scores)
    return list(zip(titles, instructions, scores))



st.markdown("<h1 style='text-align: center; color: White;'>NOURISH-TRACK</h1>", unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
img = "https://greeninitiatives.cn/wp-content/uploads/2021/07/update-resize.jpg"
st.image(img,use_column_width=True)
st.markdown("Welcome to Nourish Track, We are here to nourish you to health through food. Afterall we are what we eat !!!")
Ailment = ['<select>','Flu','Musscle Pain','Stomach Pain','Headache',
'Fever','Cold','Cough','Dizziness','Vomitting',
'Diabetes','Low Blood Pressure','High Blood Pressure',
'Body Ache','Breathing Trouble','Running Nose','Dengue',
'Iron Deficiency','Anemia','Diarrhea','Blood Loss',
'Infection','Lung Disease','Melanoma','Nutritional Deficiency',
'Obesity','Tuberculosis','Acute Pain','Post Covid','Cancer',
'Epilepsy','Kidney Disease','Liver Disease']
ingr = pd.read_csv("data/disease_ingredient.csv")

try:
    selected = st.selectbox("Enter the condition you're trying to recover from:", Ailment)
    ingredients = serve(ingr, selected)
    MAPPING = {"vit_a": "Vitamin A", "vit_c": "Vitamin C", "protein(g)": "Protein", "sat_fat": "Saturated Fats", "carbs":"Carbs", 'iron':"Iron", 'trans_fat':"Trans fat","energy":"Energy", 'cholesterol':"Cholesterol", 'sodium':"Sodium", 'fiber':"Fiber", 'sugars':"Sugars", 'calcium':"Calcium"}
    REVERSE = {v: k for (k, v) in MAPPING.items()}
    ingredients = [MAPPING.get(i, i) for i in ingredients]
    st.markdown("Depending on your selection, the following nutrients must be utilized in your recipes. If you would like to include additional nutrients please select from the dropdown:")
    final_ing = st.multiselect(label="Ingredients", options=["Vitamin A", "Vitamin C", "Protein", "Saturated Fats", "Carbs", "Iron", "Trans fat", "Cholesterol", "Sodium", "Fiber", "Sugars", "Calcium", "Energy"], default=ingredients)
    st.markdown("Kindly check the items you are allegic to: ")
    Milk,Eggs,Fish,Crab = st.columns(4)
    Milk = Milk.checkbox('Milk')
    Eggs = Eggs.checkbox('Egg')
    Fish = Fish.checkbox("Fish")
    Crab = Crab.checkbox("Crab")
    Shrimp, Peanuts, Wheat, Soybeans = st.columns(4)
    Shrimp = Shrimp.checkbox("Shrimp")
    Peanuts = Peanuts.checkbox("Peanuts")
    Wheat = Wheat.checkbox("Wheat")
    Soybeans = Soybeans.checkbox("Soybeans")
    nono_list=[]
    if Milk == "Milk":
        nono_list.append("Milk")
    if Eggs == "Egg":
        nono_list.append("Egg")
    if Fish == "Fish":
        nono_list.append("Fish")
    if Shrimp == "Shrimp":
        nono_list.append("Shrimp")
    if Peanuts == "Peanuts":
        nono_list.append("Peanuts")
    if Wheat == "Wheat":
        nono_list.append("Wheat")
    if Soybeans == "Soybeans":
        nono_list.append("Soybeans")
    

    final_ing = [REVERSE.get(i, i) for i in final_ing]

    dishes = read_file_and_match('data/ingr_to_food.csv', 'data/cleaned-recipie.csv', final_ing, nono_list)
    for item in dishes:
        name_dish = item[0]
        recipe = item[1]
        #col1,col2=st.columns(2)
        st.markdown(f"<h2 style='text-align: center; color: grey;'>{name_dish}</h2>", unsafe_allow_html=True)
        url_Addr = openai.Image.create(prompt=name_dish, n=1, size="256x256")
        imag_url = url_Addr["data"][0]["url"]
        #st.image(imag_url)
        c1, c2, c3 = st.columns([0.2, 0.25, 0.2])
        c2.image(imag_url, use_column_width=True)
        st.markdown(recipe)
        

except IndexError as e:
    st.write("Please select an Option !")
