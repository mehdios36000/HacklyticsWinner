from typing import List

import numpy as np
import pandas as pd
from pandas import DataFrame


def nut_norm_onehot(components: List[str]):
    array = np.zeros([len(NUTRIENTS)])

    for c in components:
        c = c.strip().lower()
        assert c in NUTRIENTS, [c, NUTRIENTS]
        array[NUTRIENTS_POSITION[c]] = np.sqrt(len(components))

    return array


def read_file_and_match(ingredient_food: str, cleaned_recipe: str, nutrients):
    vector = nut_norm_onehot(nutrients)
    print(len(vector))
    assert len(vector) == len(NUTRIENTS)

    if_df = pd.read_csv(ingredient_food)
    cr_df = pd.read_csv(cleaned_recipe)
    print(if_df.shape, cr_df.shape)
    # Filter out all zeros
    # if_non_zero = np.linalg.norm(if_df.loc[:, NUTRIENTS].to_numpy(), axis=-1) > 1e-8
    # if_df = if_df.iloc[if_non_zero]

    # cr_non_zero = np.linalg.norm(cr_df.loc[:, FOODS].to_numpy(), axis=-1) > 1e-8
    # cr_df = cr_df.iloc[cr_non_zero]

    return match_ingredients_and_recipe(if_df, cr_df, vector)


def match_ingredients_and_recipe(if_df: DataFrame, cr_df: DataFrame, vector):
    if_df = if_df.loc[:, ["Ingredient"] + NUTRIENTS]
    cr_df = cr_df.loc[:, ["Title"] + FOODS]

    # ingredients x nutrients
    if_df_mat = if_df.loc[:, NUTRIENTS].to_numpy().astype("float")
    if_df_mat /= np.linalg.norm(if_df_mat, axis=-1, keepdims=True) + 1e-8

    # recipes x ingredients
    cr_df_mat = cr_df.loc[:, FOODS].to_numpy().astype("float")
    cr_df_mat /= np.linalg.norm(cr_df_mat, axis=-1, keepdims=True) + 1e-8

    print(cr_df_mat.shape, if_df_mat.shape)
    match_score = np.einsum("in,ri->rn", if_df_mat, cr_df_mat)

    return match_score


FOODS = [
    f.strip()
    for f in "agave nectar,alcohol,alfalfa,almond butter,almond milk,almonds,american cheese,anchovies,apple,apple cider,apple juice,apple pie,applesauce,apricots,artic char,artichokes,arugula,asparagus,avocado,baby carrots,bacon,bagels,baked beans,baked potatoes,balsamic vinegar,banana,banana with peel,barbecue sauce,barley,basil,bean sprouts,bean(seed),beef,beer,beets,bell peppers,berries,biscuits,bison,black beans,blackberries,blue cheese,blueberries,blueberry pie,bok choy,bologna,brazil nuts,bread,bread crumbs,breadsticks,brie cheese,brisket,broccoli,broth,brown rice,brown sugar,brownies,brussels sprouts,bulgur,buns,burgers,burritos,butter,buttermilk,cabbage,caesar dressing,caesar salad,cakes,calamari,calzones,camembert cheese,candies,cantaloupe,capers,cappuccino,carp,carrot,carrot cake,cashews,catfish,cauliflower,celery,celery root,cereal,cereal bars,challah,champagne,chard,chayote squash,cheddar cheese,cheese,cheese pizza,cheeseburgers,cheesecake,cherries,cherry pie,cherry tomatoes,chestnuts,chia seeds,chicken,chicken apple sausage,chicken breast,chicken drumsticks,chicken nuggets,chicken salad,chicken soup,chicken thighs,chicken wings,chickpeas,chilaquiles,chili,chimichangas,chips,chive,chocolate,chocolate cake,chocolate chip cookies,chocolate milk,chow mein,chowders,chutney,cilantro,clams,cobbler,cocoa,coconut milk,coconuts,cod,coffee,coffee creamer,colby cheese,coleslaw,collards,cookies,corn,corn chips,corn dogs,corn nuts,corn on the cob,corn starch,cornbread,corned beef,cornmeal,cottage cheese,country rice,couscous,crab,crackers,cranberries,cranberry juice,crawfish,cream,cream cheese,crepes,crispbread,croissants,croutons,cucumbers,cupcakes,curries,custard,dark chocolate,dates,donuts,duck,dumplings,edamame,eel,egg rolls,egg salad,egg whites,egg yolks,eggnog,eggplant,eggs,empanadas,enchiladas,endive,energy drinks,english muffins,fajitas,falafel,fennel,feta cheese,figs,fish,fish oil,flatbread,flounder,flour,focaccia,french dressing,french fries,french toast,fried chicken,fried eggs,fried rice,fritters,frostings,frozen yogurt,fruit cocktail,fruit punch,fruit salad,fudge,garden salad,garlic,garlic bread,gelatin,ginger,gnocchi,goat cheese,gorgonzola cheese,gouda cheese,goulash,granola,granola bars,grape juice,grapefruit juice,grapefruits,grapes,gravy,greek salad,greek yogurt,green beans,green onions,green peas,grilled chicken,grits,ground beef,ground chicken,ground pork,ground turkey,guacamole,gumbo,gyros,haddock,half and half,halibut,ham,hamburgers,hard boiled eggs,hard cider,hash browns,havarti cheese,herring,hominy,honey,honeydew melons,horseradish,hot chocolate,hot dogs,hummus,ice cream cones,ice cream soda,ice creams,ice pop,iced tea,india pale ale beer,italian dressing,jalapenos,jambalaya,jams,jerky,jicama,kale,ketchup,kidney beans,kimchi,kiwi,lager,lamb,lamb chops,lasagna,latte,leeks,lemon,lemon juice,lemonade,lentils,lettuce,licorice,light beer,lima beans,lime,lo mein,lobster,macadamia nuts,macaroni,macaroni and cheese,mackerel,mahi mahi,mandarin oranges,mangos,maple syrup,margarine,margarita,marshmallows,mashed potatoes,mayonnaise,meatballs,meatloaf,mexican cheese,milk,milk shakes,millet,miso soup,mixed greens,mixed nuts,mixed vegetables,mousse,mozzarella cheese,muenster cheese,muesli,muffins,multigrain bread,mushroom,mussels,mustard,mustard greens,naan,nachos,nectar,nectarines,noodles,nopales,nougat,nut cheese,nutrition bars,nuts,oatmeal,oats,octopus,oil,okra,olive oil,olives,omelets,onion rings,onions,orange,orange juice,orange with peel,oregano,orzo,oysters,paella,pancakes,papayas,parmesan cheese,parsley,parsnips,pasta,pasta salad,pasta sauce,pastrami,pastries,pate nutrition,peach,peaches,peanut butter,peanuts,pears,peas,pecan pie,pecans,pepper,pepperoni,pepperoni pizza,pesto,pickles,pie crust,pies,pilaf,pine nuts,pineapple,pinto beans,pistachios,pita bread,pizza,pizza dough,pizza sauce,plate only,plums,poached eggs,polenta,pomegranate,popcorn,pork,pork chops,pot pies,potato bread,potato chips,potato salad,potato skins,potatoes,pretzels,protein powder,provolone cheese,prunes,puddings,pumpkin seeds,pumpkins,quesadillas,quiche,quinoa,radishes,raisin bran,raisin bread,raisins,ranch dressing,raspberries,ravioli,red potatoes,refried beans,relish,ribs,rice,rice cakes,rice noodles,risotto,roast beef,roast chicken,roast pork,roast turkey,roasted potatoes,rolls,romano cheese,root beer,rosemary,rum,rye bread,salad dressing,salads,salami,salmon,salsa,salt,samosas,sandwich cookies,sandwiches,sardines,sauerkraut,sausage,scallops,scones,scrambled eggs,seafood,seaweed,seeds,shallots,sherbet,shrimp,skim milk,smoked salmon,smoothies,snapper,snow peas,soft serve ice creams,sorbet,souffle,sour cream,sourdough bread,soy milk,soy nuts,soy sauce,soy sausage,soy yogurt,spaghetti,spinach (cooked),spinach (raw),spreads,spring rolls,squash,squid,steak,stews,stout beer,strawberries,string cheese,strudels,stuffing,succotash,sugar,sun dried tomatoes,sundaes,sunflower seeds,sushi,sweet potato,sweet rolls,swiss cheese,swordfish,syrup,tabouli,taco salad,taco shells,tacos,tahini,tamales,taquitos,tatsoi,tea,tempeh,tempura,teriyaki sauce,thyme,tilapia,toast,tofu,tomatillo,tomato soup,tomatoes,tortellini,tortilla,tortilla chips,tostadas,trail mix,trout,tuna,tuna salad,turkey,turkey bacon,turkey breast,turnips,turnover,veal,vegetable juice,vegetable oil,veggie burgers,vinaigrette,vinegar,vodka,wafers,waffles,walnuts,water,water chestnuts,watermelon,wheat beer,wheat berry,wheat bread,white beans,white bread,white rice,white wine,whole wheat bread,wild rice,wine,wraps,yam,yogurt,zucchini".strip().split(
        ","
    )
]
print(len(FOODS), "hello")

NUTRIENTS = "cal/g,fat(g),carb(g),protein(g),vit_a,vit_c,iron,trans_fat,sat_fat,cholesterol,sodium,carbs,fiber,sugars,calcium,protein,energy".strip().split(
    ","
)

NUTRIENTS_POSITION = {nut: pos for (pos, nut) in enumerate(NUTRIENTS)}

if __name__ == "__main__":
    print(
        read_file_and_match(
            "./data/ingr_to_food.csv",
            "./data/cleaned-recipe.csv",
            ["protein(g)", "carbs"],
        )
    )
