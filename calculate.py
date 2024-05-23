from database.db import DB
from commandline.print import Print

def calculate():
    # query = """
    #     SELECT
    #         symptoms.symptom,
    #         symptom_times.severity,
    #         (julianday(symptom_times.datetime) - julianday(ingredient_times.datetime)) * 24 AS symptom_delay,
    #         ingredients.ingredient
    #     FROM
    #         symptoms
    #     JOIN
    #         symptom_times ON symptoms.id = symptom_times.symptom_id
    #     JOIN
    #         ingredient_times ON ingredient_times.id = symptom_times.symptom_id
    #     JOIN
    #         ingredients ON ingredients.id = ingredient_times.ingredient_id
    #     WHERE
    #         symptom_delay > 0 AND symptom_delay < 24
    #     GROUP BY 
    #         ingredients.id
    #     ORDER BY
    #         COUNT(*) * AVG(symptom_times.severity) DESC
    #     LIMIT
    #         1;
        
    # """

    query = """
        SELECT
            symptoms.symptom,
            (
                SELECT
                    ingredients.ingredient
                FROM
                    symptoms AS s
                JOIN
                    symptom_times AS st ON s.id = st.symptom_id
                JOIN
                    ingredient_times AS it ON it.id = st.symptom_id
                JOIN
                    ingredients ON ingredients.id = it.ingredient_id
                WHERE
                    s.id = symptoms.id 
                    AND 
                    (julianday(st.datetime) - julianday(it.datetime)) * 24 BETWEEN 0 AND 24 
                    AND 
                    ingredients.ingredient NOT IN (SELECT ingredient FROM ignored_ingredients)
                GROUP BY
                    ingredients.id
                ORDER BY
                    COUNT(*) * AVG(st.severity) DESC
                LIMIT
                    1
            ) AS top_ingredient
        FROM
            symptoms;
    """
    results = DB.Query.query_results(query)
    print(results)
    
    Print.underline_bold("Most likely ingredient to be causing each symptom.")
    for result in results:
        symptom = result[0].title()
        ingredient = result[1] if result[1] != None else 'N/A'

        Print.key_value(symptom, ingredient)

