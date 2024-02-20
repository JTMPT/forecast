def export_in_model_format(taz):
    taz['yosh']=0

    taz.loc[taz['zonetype']=='Judea and Samaria','yosh']=1

    taz['jerusalem_city']=0

    taz.loc[taz['in_jerusal']=='yes','jerusalem_city']=1

    taz=taz.reset_index()

    return taz