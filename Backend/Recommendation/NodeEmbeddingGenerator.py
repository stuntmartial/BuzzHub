from .Ranges import *
featsCount = 224

def generateNodeEmbedding(profile):

    #Generate feature vector of ProfileModel instance

    global featsCount

    embedding = [0] * featsCount

    dobYear = profile.dateofbirth
    dobYear = int ( dobYear[len(dobYear) - 4:] )
    educationField = [eduField for eduField in profile.educationFieldString.split('#')]
    educationConcentration = [eduConc for eduConc in profile.educationConcentrationString.split('#')]
    educationDegree = [eduDeg for eduDeg in profile.educationDegreeString.split('#')]
    school = profile.school
    educationType = profile.educationType
    graduationYear = int(profile.graduationYear)
    gender = profile.gender
    hometown = profile.hometown
    locality = profile.locality
    languages = [lng for lng in profile.languagesString.split('#')]
    locale = [lc for lc in profile.localeString.split('#')]
    employers = [emp for emp in profile.employerString.split('#')]
    workStartyears = [yr for yr in profile.workStartyearString.split('#')]
    workEndyears = [yr for yr in profile.workEndyearString.split('#')]
    workLocations = [loc for loc in profile.workLocationString.split('#')]
    workPositions = [yr for yr in profile.workPositionString.split('#')]

    for featIndex in range(0,8):
        if Range_dobYear[featIndex] == dobYear:
            embedding[featIndex] = 1
            break

    for featIndex in range(8,13):
        if Range_educationField[featIndex - 8] in educationField:
            embedding[featIndex] = 1

    for featIndex in range(13,20):
        if Range_educationConcentration[featIndex - 13] in educationConcentration:
            embedding[featIndex] = 1

    for featIndex in range(20,24):
        if Range_educationDegree[featIndex - 20] in educationDegree:
            embedding[featIndex] = 1

    for featIndex in range(24,53):
        if Range_school[featIndex - 24] == school:
            embedding[featIndex] = 1
            break

    for featIndex in range(53,56):
        if Range_educationType[featIndex - 53] == educationType:
            embedding[featIndex] = 1
            break

    for featIndex in range(57,73):
       if Range_graduationYear[featIndex - 57] == graduationYear:
            embedding[featIndex] = 1
            break

    for featIndex in range(77,79):
        if Range_gender[featIndex - 77] == gender:
            embedding[featIndex] = 1
            break

    for featIndex in range(79,90):
        if Range_hometown[featIndex - 79] == hometown:
            embedding[featIndex] = 1
            break

    for featIndex in range(90,104):
        if Range_languages[featIndex - 90] in languages:
            embedding[featIndex] = 1

    for featIndex in range(125,128):
        if Range_locale[featIndex - 125] in locale:
            embedding[featIndex] = 1
    
    for featIndex in range(128,140):
        if Range_locality[featIndex - 128] == locality:
            embedding[featIndex] = 1
            break

    for featIndex in range(140,160):
        if Range_employers[featIndex - 140] in employers:
            embedding[featIndex] = 1

    for featIndex in range(160,176):
        if Range_Endyears[featIndex - 160] in workEndyears:
            embedding[featIndex] = 1
    
    for featIndex in range(176,188):
        if Range_workLocations[featIndex - 176] in workLocations:
            embedding[featIndex] = 1

    for featIndex in range(188,201):
        if Range_workPositions[featIndex - 188] in workPositions:
            embedding[featIndex] = 1

    for featIndex in range(201,223):
        if Range_workStartyears[featIndex - 201] in workStartyears:
            embedding[featIndex] = 1

    
    return embedding