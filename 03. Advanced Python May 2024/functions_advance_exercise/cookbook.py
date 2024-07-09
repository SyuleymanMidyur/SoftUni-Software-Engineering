def cookbook(*recipes):
    sorted_recipes = sorted(recipes, key=lambda x: (len(recipes) - recipes.count(x[1]), x[1], x[0]))
    cuisines = {}

    for recipe in sorted_recipes:
        recipe_name, cuisine, ingredients = recipe
        if cuisine not in cuisines:
            cuisines[cuisine] = []
        cuisines[cuisine].append((recipe_name, ingredients))

    for cuisine, recipes_list in cuisines.items():
        recipes_list.sort(key=lambda x: x[0])
        print(f"  {cuisine} cuisine contains {len(recipes_list)} recipes:")
        for recipe_name, ingredients in recipes_list:
            print(f"    * {recipe_name} -> Ingredients: {', '.join(ingredients)}")

    return f"  {cuisine} cuisine contains {len(recipes_list)} recipes:"
    return f"    * {recipe_name} -> Ingredients: {', '.join(ingredients)}"