def skill(cloud_provider):
    if cloud_provider == "azure":
        with open("resources/createElastigroupSpotVMs.yaml") as f:
            return f.read()
    else:
        with open("resources/elastigroupVm.yaml") as f:
            return f.read()
