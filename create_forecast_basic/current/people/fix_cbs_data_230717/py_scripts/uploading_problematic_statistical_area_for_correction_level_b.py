def uploading_problematic_statistical_area_for_correction_level_b(jtmt_fix_stat, stat):
    col=['STAT',
    'fix_pop',
    'fix_aprt',
    'fix_class']

    jtmt_fix_stat=jtmt_fix_stat[col].set_index('STAT')

    stat=stat.set_index('STAT')

    stat=stat.join(jtmt_fix_stat, how='left')

    return stat