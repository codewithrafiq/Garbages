def generate_category(ind, categories,cat_res):
    # print('OK')
    if(ind == len(categories)):
        return
    if categories[ind]["fk"] == "null":
        cat_res.append(categories[ind])
        generate_category(ind+1, categories,cat_res)
    else:
        generate_category(ind+1, categories,cat_res)
        fk = categories[ind]["fk"]
        id = categories[ind]["id"]
        for cat in range(len(categories)):
            if fk == categories[cat]["id"]:
                if categories[cat] not in cat_res:
                    cat_res.append(categories[cat])

        for cat in range(len(cat_res)):
            if id == cat_res[cat]["id"]:
                cat_res.pop(cat)
                break

        for cat in cat_res:
            if fk == cat["id"]:
                if "sub_categories" in cat.keys():
                    cat["sub_categories"].append(categories[ind])
                else:
                    cat["sub_categories"] = [categories[ind]]
    return cat_res