import json, os, requests
from fpdf import FPDF
from collections import Counter, OrderedDict
import functools, operator, itertools

path = './content/'
chemin_logs = os.path.join("./content/", "logs")
chemin_pdf = os.path.join("./content/", "pdf")


# ===================================================
# ===================================================
#
# Etape N°2: Conversion des fichiers de logs en fichier pdf
#
# ===================================================
# ===================================================
class PDF(FPDF):
    def footer(self):
        if self.page_no() != 1:
            self.set_y(-15)
            self.set_font('Arial', 'B', 10)
            self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


for file in os.listdir(path+"logs"):
    pdf = PDF()
    pdf.set_auto_page_break(True, margin=7)
    pdf.alias_nb_pages()
    pdf.add_page()
    transfert = []
    achat_action = []
    fondation = []
    dirigeant = []
    vente = []
    achat = []
    war_reason = 0
    raison_guerre = []
    plugin_raison_guerre = []
    result_raison_guerre = []
    début_guerre = []
    forfait_guerre = []
    guerre_gagnée = []
    staff_annulation_guerre = []
    joueur_annulation_guerre = []
    plugin_annulation_guerre = []
    banque_retrait = []
    banque_depot = []
    assaut = []
    warzone = []
    meteo = 0
    meteo_lunaire = 0
    adminshop_global = 0
    adminshop = []
    mute = []
    tempban = []
    jm = []
    mutecommerce = []
    tracteur_list = ["Seeder", "Fertilizer", "Harvester", "Plower", "Tractor", "Tank"]
    tracteur_detruit = []
    tracteur_pose = []
    tracteur_donne = []
    item_speciaux = []
    item_spatial = []
    item_missile = []
    he_tool = []
    he_search = []
    colony_demande = []
    taxe_pays_preleve = []
    taxe_pays_define = []
    trading_pourcentage = []
    trading_investissement = []
    trading_generation = []
    trading_gains = []
    result_trading = []
    result_warzone = []
    result_elec = []
    elec_quantite = []
    elec_price = []
    total_elect = 0
    petrol_price = []
    petrol_quantite = []
    result_petrol = []
    total_petrol = 0
    agricole_price = []
    result_agricole = []
    total_agricole = 0
    casino_price = []
    result_casino = []
    immo_price = []
    result_immo = []
    avocat_price = []
    result_avocat = []
    creation_ent = []
    injection_ent = []
    disband_ent = []
    unclaim = []
    result_unclaim = []
    claim = []
    result_claim = []
    pillage = []
    result_pillage = []
    surclaim = []
    result_surclaim = []
    powerboost_joueur = []
    result_powerboost_joueur = []
    powerboost_pays = []
    get_item_auction = 0
    create_auction = []
    result_create_auction = []
    augmente_auction = []
    result_augmente_auction = []
    end_auction = []
    connect_end_auction = ""
    result_end_auction = []
    remove_auction = []
    achat_hdv = []
    vente_hdv = []
    hdv = 0
    pub_hdv = 0
    divorce = 0
    notation = []
    notation_global = 0
    bourse_action = []
    bourse_action_global = 0
    prime_entreprise = []
    global_journal = []
    death_list = ["a été tué par", "burned to death", "a succombé", "s'est écrasé au sol", "s'est fait exploser",
                  "death.attack.weapon", "withered away", "avec un m249", "s'est noyé", "fell from a high place",
                  "a essayé de nager dans la lave", "suffucated in a wall", "est tombé dans le néant",
                  "was pricked to death"]
    delete_char = ["[INFO]", "[Guide]", "[Modo§aT§2]", "[Modo]", "[Modo§c+§2]", "[Premium]", "[Légende]", "[Héros]",
                   "[Streamer]", "[Joueur]", "[Maf]", "[Cdt]", "[Avocat]", "[Adj]", "[Merc]", "[Srgt]", "[§4☠§8]",
                   "[§4⚔§8]", "§1", "§2", "§3", "§4", "§5", "§6", "§7", "§8", "§9", "§a", "§b", "§c", "§d", "§e", "§f",
                   "✹", "★", "●", "✦", "�", "❖", "⭐", "✜", "✛", "︽", "︿", "－", "⁑", "✚", "✵", "❆", "✠", "❈", "❄", "✍",
                   "⚖", ".", "۩", "◊", "⚘", "✜", "✛", "︽", "︿", "－", "⁑", "✚", "✵", "❆", "✠", "❈", "❄", "✍", ".", "✎",
                   "۩", "◊", "⚘", "⚔", "✙", "✧", "avec Glaive en Emeraude"]
    death = []
    duel_win = []
    duel_loose = []
    duel_amount = 0
    chestshop = []
    access_player_true = []
    access_player_false = []
    meteore = []
    obscur = ["MAGNESIUM", "GALLIUM", "NIOBIUM"]
    minerais_bois = {}

    if file.endswith('.log'):

        pdf.set_font("Arial", size=20)
        pdf.cell(40, 10, "=======================================", ln=1)
        pdf.cell(40, 10, file, ln=1)
        pdf.cell(40, 10, "Résumé de la journée", ln=1)
        pdf.cell(40, 10, "=======================================", ln=1)

        pdf.set_font("Arial", size=13)
        page_paiement = pdf.add_link()
        pdf.cell(40, 8, "1  . Les transferts d'argent Joueurs", ln=1, link=page_paiement)
        page_transaction = pdf.add_link()
        pdf.cell(40, 8, "2  . Les retraits & dépôts dans les banques", ln=1, link=page_transaction)
        page_achat = pdf.add_link()
        pdf.cell(40, 8, "3  . Les achats / ventes de pays et achat actions", ln=1, link=page_achat)
        page_leader = pdf.add_link()
        pdf.cell(40, 8, "4  . Les pays créés / changement de chef et achat illégal de pays", ln=1, link=page_leader)
        page_notations = pdf.add_link()
        pdf.cell(40, 8, "5  . Les bourses des notations et des actions", ln=1, link=page_notations)
        page_claim = pdf.add_link()
        pdf.cell(40, 8, "6  . Les informations sur les claims", ln=1, link=page_claim)
        page_guerre = pdf.add_link()
        pdf.cell(40, 8, "7  . Les informations sur les guerres et assauts", ln=1, link=page_guerre)
        page_warzone = pdf.add_link()
        pdf.cell(40, 8, "8  . Les gains warzone", ln=1, link=page_warzone)
        page_argent = pdf.add_link()
        pdf.cell(40, 8, "9  . Les rentrées d'argent Staff", ln=1, link=page_argent)
        page_hdv = pdf.add_link()
        pdf.cell(40, 8, "10  . Les achats & ventes HDV", ln=1, link=page_hdv)
        page_chestshop = pdf.add_link()
        pdf.cell(40, 8, "11  . Les chest Shop", ln=1, link=page_chestshop)
        page_staff = pdf.add_link()
        pdf.cell(40, 8, "12  . Les commandes staff utilisées", ln=1, link=page_staff)
        page_tracteur = pdf.add_link()
        pdf.cell(40, 8, "13  . Les informations sur les tracteurs", ln=1, link=page_tracteur)
        page_colonie = pdf.add_link()
        pdf.cell(40, 8, "14 . Les informations sur les colonies", ln=1, link=page_colonie)
        page_entreprise = pdf.add_link()
        pdf.cell(40, 8, "15 . Les informations sur les entreprises", ln=1, link=page_entreprise)
        page_prime = pdf.add_link()
        pdf.cell(40, 8, "16 . Les primes des entreprise", ln=1, link=page_prime)
        page_powerboost = pdf.add_link()
        pdf.cell(40, 8, "17 . Le Power Boost", ln=1, link=page_powerboost)
        page_enchere = pdf.add_link()
        pdf.cell(40, 8, "18 . Les enchères", ln=1, link=page_enchere)
        page_deaths = pdf.add_link()
        pdf.cell(40, 8, "19 . Les Morts", ln=1, link=page_deaths)
        page_duel = pdf.add_link()
        pdf.cell(40, 8, "20 . Les Duels", ln=1, link=page_duel)
        page_obscur = pdf.add_link()
        pdf.cell(40, 8, "21 . Les minerais obscurs", ln=1, link=page_obscur)
        page_access = pdf.add_link()
        pdf.cell(40, 8, "22 . Les access pays", ln=1, link=page_access)
        page_meteore = pdf.add_link()
        pdf.cell(40, 8, "23 . Les météores", ln=1, link=page_meteore)

        with open(path+"logs/" + file, "r", encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            if u'\uf716' in line:
                line = line.replace(u'\uf716', "")
            # ===================Catégorie transaction joueur==========================
            if "issued server command: /pay" in line:
                sto = line.split()
                if len(sto) == 10:
                    try:
                        (float(sto[9]))
                        if float(sto[9]) > 5000:
                            transfert.append(sto)

                    except ValueError:
                        continue

            elif "vient d'acheter" in line and "pour une somme totale de" in line:
                sto = line.split()
                achat_hdv.append([sto[4], sto[-3]])
                vente_hdv.append([sto[-9], sto[-3]])
            # ===================Catégorie transaction joueur==========================

            # ===================Catégorie duel==========================
            elif "AFTER WIN DUEL" in line:
                sto = line.split()
                duel_win.append([sto[4], sto[6].replace("$", "")])
                duel_loose.append([sto[-1], sto[6].replace("$", "")])
            # ===================Catégorie duel==========================

            # ===================Catégorie ChestShop==========================
            elif "created a shop" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[ChestShop]")
                sto.remove("a")
                sto.remove("shop")
                chestshop.append(sto)

            elif "[ChestShop]" in line and "bought" in line and "adminshop" not in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[ChestShop]")
                sto.remove("at")
                chestshop.append(sto)
            # ===================Catégorie ChestShop==========================

            # ===================Catégorie chagement leader==========================
            elif "est le nouveau dirigeant du pays" in line:
                sto = line.split()
                sto[3] = sto[3].replace('\x1b[0;33;22m', '')
                sto[5] = sto[5].replace('\x1b[0;37;1m', '')
                dirigeant.append(sto)

            elif "vient de fonder le pays" in line and "m ONU >>" in line:
                sto = line.split()
                sto[6] = sto[6].replace('\x1b[0;37;1m', '')
                fondation.append([sto[0], sto[1], sto[6], sto[7], sto[8], sto[9], sto[10], sto[11], sto[12], sto[13]])


            elif "ACHAT PAYS" in line:
                sto = line.split()
                sto.remove("[INFO]")
                achat.append(sto)


            elif "MISE EN VENTE" in line:
                sto = line.split()
                if sto[-1] != '-1$':
                    vente.append(sto)

            elif "ACHAT ACTION :" in line:
                sto = line.split()
                achat_action.append(sto)

            # ===================Catégorie chagement leader==========================

            # ===================Catégorie guerre==========================
            elif "DONE BY" in line:
                if war_reason == 1:
                    raison_guerre.append(" Aucune raison de guerre indiquée")
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsUtils]")
                sto.remove("DONE")
                sto.remove("BY")
                raison_guerre.append(sto)
                war_reason = 1

            elif ("Add war" in line or "CANCELLED" in line) and war_reason == 1:
                if "Add war" in line:
                    raison_guerre.append(" => Raison de guerre fournie")
                else:
                    sto = line.split()
                    raison_guerre.append(" => Raison de guerre non fournie: " + " ".join(sto[6:len(sto) + 1]))
                war_reason = 0

            elif "Add war" in line and war_reason == 0:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsUtils]")
                plugin_raison_guerre.append(sto)


            elif "START WAR" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsGUI]")
                sto.remove("between")
                début_guerre.append(sto)

            elif "SURREND WAR" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsGUI]")
                sto.remove("WAR")
                sto.remove("AGAINST")
                sto.remove("APPLY")
                forfait_guerre.append(sto)

            elif "War won" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsUtils]")
                guerre_gagnée.append(sto)

            elif "/wars remove" in line:
                sto = line.split()
                staff_annulation_guerre.append(sto[3] + " a annulé une guerre contre " + sto[-2] + " et " + sto[-1])

            elif "Change status of war request between" in line and "to cancelled" in line:
                sto = line.split()
                joueur_annulation_guerre.append(
                    "Une ation joueur a annulé la guerre entre " + sto[10] + " et " + sto[12])

            elif "Cancel war between" in line:
                sto = line.split()
                plugin_annulation_guerre.append(
                    "Guerre stopée entre " + sto[7] + " et " + sto[9] + " car: " + ' '.join(sto[10:-1]))

            elif "[INFO] [NationsUtils] Apply reward" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsUtils]")
                guerre_gagnée.append(sto)
            # ===================Catégorie guerre==========================

            # ===================Catégorie transaction banque==========================
            elif "TRANSACTION BANK - TAKE" in line:
                sto = line.split()
                sto[9] = sto[9].replace('$', '')
                sto[9] = float(sto[9])
                if sto[9] > 5000:
                    sto.remove("[INFO]")
                    sto.remove("[NationsGUI]")
                    sto.remove("TRANSACTION")
                    sto.remove("BANK")
                    banque_retrait.append(sto)

            elif "TRANSACTION BANK - DEPOSIT" in line:
                sto = line.split()
                sto[9] = sto[9].replace('$', '')
                sto[9] = float(sto[9])
                if sto[9] > 5000:
                    sto.remove("[INFO]")
                    sto.remove("[NationsGUI]")
                    sto.remove("TRANSACTION")
                    sto.remove("BANK")
                    banque_depot.append(sto)

            # ===================Catégorie transaction banque==========================

            # ===================Catégorie Notations==========================
            elif "vient de recevoir une bourse" in line:
                sto = line.split()
                notation.append([sto[6], sto[-2]])
                notation_global += int(float(sto[-2]))

            elif "vient de percevoir" in line:
                sto = line.split()
                bourse_action.append([sto[6], round(float(sto[10].replace("$", "")), 2), sto[-1]])
                bourse_action_global += round(float(sto[10].replace("$", "")), 2)

            # ===================Catégorie Notations==========================

            # ===================Catégorie assaut==========================
            elif "mDébut d'assaut" in line:
                action = "Début d'assaut"
                sto = line.split()
                date = sto[0:2]
                date.append(action)
                country = sto[9:12]
                country.pop(1)
                country[0] = country[0].replace("\x1b[0;32;1m", "").replace("\x1b[m", "")
                country[1] = country[1].replace("\x1b[0;32;1m", "").replace("\x1b[m", "")
                assaut.append(date + country)

            elif "vient aider" in line and "[INFO]" in line:
                sto = line.split()
                action = "vient aider"
                assaut.append([sto[0], sto[1], sto[5].replace("[0;32;1m", ""), "vider aider", sto[8]])

            elif "vient de lancer un missile" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto[2] = sto[2].replace("\x1b[0;37;22m\x1b[3m", "")
                sto[-1] = sto[-1].replace("\x1b[m", "")
                assaut.append(sto)

            elif "exploded in" in line:
                sto = line.split()
                sto.remove("in")
                sto.remove("[INFO]")
                assaut.append(sto)

            elif "mgagne contre" in line:
                action = "Fin d'assaut"
                sto = line.split()
                date = sto[0:2]
                date.append(action)
                country = sto[5:11]
                country.pop(4)
                country.pop(3)
                country.pop(2)
                country[1] = "gagne contre"
                country[0] = country[0].replace("\x1b[0;32;1m", "")
                country[2] = country[2].replace("\x1b[0;31;1m", "")
                assaut.append(date + country)
                assaut.append("---------")
            # ===================Catégorie assaut==========================

            # ===================Catégorie warzone==========================
            elif "[WarZone] Add" in line:
                sto = line.split()
                warzone.append(' '.join(sto[5:9]))
            # ===================Catégorie warzone==========================

            # ===================Rentrée argent==========================
            elif "mMétéo >" in line:
                meteo = meteo + 1

            elif "Météo Lunaire" in line:
                meteo_lunaire = meteo_lunaire + 1

            elif "from adminshop" in line:
                sto = line.split()
                adminshop.append([sto[4], float(sto[-8]), ' '.join(sto[6:8])])
                adminshop_global += float(sto[-8])

            elif "mettre en vente sur l'hôtel des ventes" in line:
                pub_hdv += 1

            elif "séparer de son" in line:
                divorce += 1
            # ===================Rentrée argent==========================

            # ===================Catégorie Staff==========================
            elif ": /jm " in line:
                sto = line.split()
                sto.remove("[INFO]")
                try:
                    sto.remove("issued")
                except:
                    continue
                try:
                    sto.remove("alias:")
                except:
                    continue
                jm.append(sto)

            elif ": /mute " in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("issued")
                sto.remove("server")
                sto.remove("command:")
                mute.append(sto)


            elif ": /tempban " in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("issued")
                sto.remove("server")
                sto.remove("command:")
                tempban.append(sto)

            elif ": /mutecommerce " in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("issued")
                sto.remove("alias:")
                mutecommerce.append(sto)

            elif ": /he tool" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("issued")
                sto.remove("server")
                sto.remove("command:")

                he_tool.append(sto)

            elif ": /he search" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("issued")
                sto.remove("server")
                sto.remove("command:")
                he_search.append(sto)
            # ===================Catégorie Staff==========================

            # ===================Catégorie Workstation==========================

            elif any(ele in line for ele in tracteur_list) and "broken" in line:
                sto = line.split()
                sto.remove("[INFO]")
                tracteur_detruit.append(sto)

            elif any(ele in line for ele in tracteur_list) and "spawn" in line:
                sto = line.split()
                sto.remove("[INFO]")
                tracteur_pose.append(sto)

            elif "WITH WORKSTATION" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NGVehicles]")
                sto.remove("WITH")
                sto.remove("WORKSTATION")
                sto.remove("PLAYER")

                if "3639" in line:
                    tracteur_donne.append(sto)

                elif "2268" in line or "2269" in line or "2270" in line or "2270" in line or "2271" in line or "2272" in line or "2273" in line or "0809:0" in line:
                    if sto[-1] == "2268:0":
                        sto[-1] = "Pioche electrique"
                    elif sto[-1] == "2269:0":
                        sto[-1] = "Pioche electrique améliorée"
                    elif sto[-1] == "2270:0":
                        sto[-1] = "Hâche electrique"
                    elif sto[-1] == "2271:0":
                        sto[-1] = "Hâche electrique améliorée"
                    elif sto[-1] == "2272:0":
                        sto[-1] = "Pelle electrique"
                    elif sto[-1] == "0809:0":
                        sto[-1] = "Botte collantes"
                    item_speciaux.append(sto)

                elif "5109:0" in line or "5108:0" in line or "5110:0" in line or "10162:0" in line:
                    if sto[-1] == "5109:0":
                        sto[-1] = "tuyère"
                    elif sto[-1] == "5108:0":
                        sto[-1] = "Moteur Vulcain"
                    elif sto[-1] == "5110:0":
                        sto[-1] = "Moteur Propergol"
                    elif sto[-1] == "10162:0":
                        sto[-1] = "Fusée"
                    item_spatial.append(sto)

                elif "19483:9" in line or "19483:29" in line or "19483:30" in line or "19488:0" in line:
                    if sto[-1] == "19483:9":
                        sto[-1] = "Contagious"
                    elif sto[-1] == "19483:29":
                        sto[-1] = "Megasonic"
                    elif sto[-1] == "19483:30":
                        sto[-1] = "EarthQuake"
                    elif sto[-1] == "19488:0":
                        sto[-1] = "Rocket Launcher"
                    item_missile.append(sto)

            # ===================Catégorie Workstation==========================

            # ===================Catégorie Colonie==========================
            elif "vient de faire une demande de colonie sur" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[Factions]")
                colony_demande.append(sto)

            elif "payer la taxe empire" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[Factions]")
                taxe_pays_preleve.append(sto)

            elif " /f colonytax" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("issued")
                sto.remove("server")
                sto.remove("command:")
                taxe_pays_define.append(sto)

                # ===================Catégorie Colonie==========================


            # ===================Catégorie Entreprise==========================
            elif "Invest total de" in line:
                sto = line.split()
                trading_investissement.append(sto)

            elif "Pourcentage de rendement" in line:
                sto = line.split()
                trading_pourcentage.append(sto)

            elif "Argent généré par" in line:
                sto = line.split()
                trading_generation.append(sto)

            elif "Argent généré par" in line:
                sto = line.split()
                trading_generation.append(sto)

            elif "pour la raison performance" in line:
                sto = line.split()
                trading_gains.append(sto)


            elif "MW à l'entreprise" in line:
                sto = line.split()
                elec_quantite.append([sto[10], int(sto[6])])

            elif "pour la raison electricity" in line:
                sto = line.split()
                sto[6] = sto[6].replace("$", '')
                elec_price.append([sto[11], float(sto[6])])
                total_elect += float(sto[6])

            elif "litres à l'entreprise" in line:
                sto = line.split()
                petrol_quantite.append([sto[10], int(sto[6])])

            elif "pour la raison petrol" in line:
                sto = line.split()
                sto[6] = sto[6].replace("$", '')
                petrol_price.append([sto[11], float(sto[6])])
                total_petrol += float(sto[6])


            elif "pour la raison sell_cereals" in line:
                sto = line.split()
                sto[6] = sto[6].replace("$", '')
                agricole_price.append([sto[11], float(sto[6])])
                total_agricole += float(sto[6])

            elif "pour la raison coin_buy" in line:
                sto = line.split()
                sto[6] = sto[6].replace("$", '')
                casino_price.append([sto[11], float(sto[6])])

            elif "pour la raison parcelle_rent" in line:
                sto = line.split()
                sto[6] = sto[6].replace("$", '')
                immo_price.append([sto[11], float(sto[6])])

            elif "pour la raison contract" in line:
                sto = line.split()
                sto[6] = sto[6].replace("$", '')
                avocat_price.append([sto[11], float(sto[6])])

            elif "Deposit bonus" in line:
                sto = line.split()
                prime_entreprise.append([sto[-1].split("(")[0], sto[9], int(sto[7].replace("$", ""))])

            elif "Creation de l'entreprise" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsJob]")
                creation_ent.append(sto)

            elif "Injection apport" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsJob]")
                injection_ent.append(sto)

            elif "[NationsJob] Disband enterprise" in line or "Reversement du capital" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("[NationsJob]")
                disband_ent.append(sto)

            # ===================Catégorie Entreprise==========================

            # ===================Catégorie RP journal==========================
            elif "Command run by remote user" in line and "journal" in line:
                sto = line.split()
                global_journal.append(sto[-1].replace("&6", "").replace("'", ""))

            # ===================Catégorie RP journal==========================

            # ===================Catégorie Claim==========================
            elif "[0;33;1msell" in line:
                sto = line.split()
                sto[3] = sto[3].replace("\x1b[0;33;22m\x1b[0;37;1m", "").replace("[0;33;22m[0;35;1m", "")
                sto[-1] = sto[-1].replace("\x1b[0;33;22m\x1b[0;37;1m", "").replace("\x1b[m", "").replace(
                    "[0;33;22m[0;35;1m", "")
                unclaim.append(''.join(sto[3] + " " + sto[4] + " " + str(sto[-1])))

            elif "[0;33;1mbuy" in line:
                sto = line.split()
                sto[3] = sto[3].replace("\x1b[0;33;22m\x1b[0;37;1m", "").replace("[0;33;22m[0;35;1m", "")
                sto[-1] = sto[-1].replace("\x1b[0;33;22m\x1b[0;37;1m", "").replace("\x1b[m", "").replace(
                    "[0;33;22m[0;35;1m", "")
                claim.append(''.join(sto[3] + " " + sto[4]))

            elif "[0;33;1mpillage" in line:
                sto = line.split()
                sto[3] = sto[3].replace("\x1b[0;33;22m\x1b[0;37;1m", "").replace("[0;33;22m[0;35;1m", "")
                sto[-1] = sto[-1].replace("\x1b[0;33;22m\x1b[0;37;1m", "").replace("\x1b[m", "").replace(
                    "[0;33;22m[0;35;1m", "")
                pillage.append(''.join(sto[3] + " " + sto[4] + " " + str(sto[-1])))

            elif "[0;33;1mconquer" in line:
                sto = line.split()
                sto[3] = sto[3].replace("\x1b[0;33;22m\x1b[0;37;1m", "").replace("[0;33;22m[0;35;1m", "")
                sto[-1] = sto[-1].replace("\x1b[0;33;22m\x1b[0;37;1m", "").replace("\x1b[m", "").replace(
                    "[0;33;22m[0;35;1m", "")
                surclaim.append(''.join(sto[3] + " " + sto[4] + " " + str(sto[-1])))
                # ===================Catégorie RP Claim==========================

            # ===================Catégorie PowerBoost==========================
            elif "Powerboost to" in line:
                sto = line.split()
                powerboost_joueur.append([sto[9], sto[6].replace("+", "")])

            elif "POWERBOOST DE" in line:
                sto = line.split()
                if float(sto[11]) == 0 or float(sto[9]) - float(sto[11]) > 20:
                    powerboost_pays.append([sto[7], str(round(float(sto[9]), 0)), str(round(float(sto[11]), 0))])

            # ===================Catégorie PowerBoost==========================

            # ===================Catégorie enchères==========================
            elif "[Auction]" in line:
                if "New Player auction" in line:
                    get_item_auction = 1
                    sto = line.split()
                    create_auction.append([sto[9], sto[14]])

                elif "New Player bid" in line and ("refund" in line or "withdraw" in line):
                    sto = line.split()
                    augmente_auction.append([''.join(sto[8] + " " + sto[11]), sto[9].replace("$", "")])

                elif "End of auction" in line:
                    sto = line.split()
                    if connect_end_auction != "":
                        end_auction.append(" mais l'acheteur n'était pas connecté pour recevoir son item")
                        connect_end_auction = ""

                    end_auction.append(sto[-1] + " a reçu " + sto[9] + " pour la vente")
                    connect_end_auction = sto[1]

                elif "Give" in line and connect_end_auction != "":
                    sto = line.split()
                    if connect_end_auction == sto[1]:
                        end_auction.append(" et " + sto[-1] + " a reçu " + sto[6].replace("x", "") + " " + sto[7])
                        connect_end_auction = ""
                    else:
                        end_auction.append(" mais l'acheteur n'était pas connecté pour recevoir son item")
                        connect_end_auction = ""

                elif "remove" in line:
                    sto = line.split()
                    remove_auction.append(
                        "Une enchère a été annulée et " + sto[-1] + " a récupéré le montant de sa dernière enchère:" +
                        sto[9])

            elif "[INFO] [HDV]" in line and get_item_auction == 1:
                get_item_auction = 0
                sto = line.split()
                create_auction.append([sto[11].replace("x", ""), sto[12].replace("ID:(", "").replace(")", ""), sto[18]])

            # ===================Death list ==========================
            elif any(ext in line for ext in death_list):
                for x in delete_char:
                    line = line.replace(x, "")

                sto = line.split()
                for x in range(len(sto)):
                    if sto[x] == "avec":
                        sto = sto[:x]
                        break
                death.append(sto)
            # ===================Death list ==========================

            # ===================Catégorie access==========================
            elif "set access to player" in line:
                sto = line.split()
                if sto[5] != sto[10]:
                    if "to true" in line:
                        access_player_true.append([sto[0], sto[1], sto[5], sto[7], sto[10], sto[13], sto[14]])
                    else:
                        access_player_false.append([sto[0], sto[1], sto[5], sto[7], sto[10], sto[13], sto[14]])

            elif "METEOR SPAWNED IN" in line:
                sto = line.split()
                sto.remove("[INFO]")
                sto.remove("METEOR")
                sto.remove("SPAWNED")
                sto.remove("IN")

                sto[-1] = str(round(float(sto[-1].replace(",", "")), 0))
                sto[-3] = str(round(float(sto[-3].replace(",", "")), 0))
                meteore.append(''.join(sto[0] + " " + sto[1] + " " + sto[2] + ": " + sto[-3] + " " + sto[-1]))

            # ===================Minerais obscur & bois millénaire==========================
            if any(ext in line for ext in obscur) and "BY" in line:
                sto = line.split()
                if sto[-1] in minerais_bois:
                    if sto[-3] in minerais_bois[sto[-1]]:
                        minerais_bois[sto[-1]][sto[-3]] += 1
                    else:
                        minerais_bois[sto[-1]][sto[-3]] = 1
                else:
                    minerais_bois[sto[-1]] = {}
                    minerais_bois[sto[-1]][sto[-3]] = 1

            if "SPAWN OBSCURE BLOCK" in line:
                sto = line.split()
                if sto[-1] in minerais_bois:
                    if "obscur" in minerais_bois[sto[-1]]:
                        minerais_bois[sto[-1]]["obscur"] += 1
                    else:
                        minerais_bois[sto[-1]]["obscur"] = 1
                else:
                    minerais_bois[sto[-1]] = {}
                    minerais_bois[sto[-1]]["obscur"] = 1

            if "SPAWN MILLENIAL WOOD" in line:
                sto = line.split()
                if sto[-1] in minerais_bois:
                    if "bois" in minerais_bois[sto[-1]]:
                        minerais_bois[sto[-1]]["bois"] += 1
                    else:
                        minerais_bois[sto[-1]]["bois"] = 1
                else:
                    minerais_bois[sto[-1]] = {}
                    minerais_bois[sto[-1]]["bois"] = 1
            # ===================Minerais obscur==========================

            else:
                continue

        # ===================Calcul transaction joueur ==========================

        result_achat_hdv = Counter()
        for name, value in achat_hdv:
            result_achat_hdv[name] += int(value)
            hdv += int(value)

        result_achat_hdv = OrderedDict(sorted(result_achat_hdv.items()))

        result_vente_hdv = Counter()
        for name, value in vente_hdv:
            result_vente_hdv[name] += int(value)
        result_vente_hdv = OrderedDict(sorted(result_vente_hdv.items()))

        # ===================Calcul transaction joueur ==========================

        # ===================Calcul transaction joueur ==========================

        result_duel_win = Counter()
        for name, value in duel_win:
            result_duel_win[name] += int(value)
            duel_amount += int(value)

        result_duel_win = OrderedDict(sorted(result_duel_win.items()))

        result_duel_loose = Counter()
        for name, value in duel_loose:
            result_duel_loose[name] += int(value)
        result_duel_loose = OrderedDict(sorted(result_duel_loose.items()))

        # ===================Calcul transaction joueur ==========================

        # ===================Calcul bourse action ==========================
        result_bourse_action = {}
        for country, content in itertools.groupby(sorted(bourse_action, key=operator.itemgetter(0)),
                                                  key=operator.itemgetter(0)):
            data = list(content)
            result_bourse_action[country] = {"amount": sum([x[1] for x in data]), "country_take": [x[2] for x in data]}
        result_bourse_action = OrderedDict(sorted(result_bourse_action.items()))
        # ===================Calcul bourse action ==========================

        # ===================Calcul guerre ==========================
        count = 0
        for line in raison_guerre:
            if count % 2 == 0:
                sto = ' '.join(line)
                count = 1
            else:
                result_raison_guerre.append(sto + line)
                count = 0
        # ===================Calcul guerre ==========================

        # ===================Calcul transaction pays==========================
        result_take = []
        taking = []
        for take in banque_retrait:
            taking.append([take[4], take[7]])

        for take in taking:
            for take2 in taking:
                if (take[0] == take2[0] and take[1] != take2[1]):
                    if [take[0], take[1], take2[1]] not in result_take:
                        result_take.append([take[0], take[1], take2[1]])

        # ===================Calcul transaction pays==========================

        global_journal = Counter(global_journal)

        # ===================Calcul Avocat==========================
        total_avocat = {}
        for avocat in avocat_price:
            if avocat[0] not in total_avocat:
                total_avocat[avocat[0]] = avocat[1]
            else:
                total_avocat[avocat[0]] = total_avocat[avocat[0]] + avocat[1]

        for key, val in total_avocat.items():
            result_avocat.append([key, val])

        # ===================Calcul Avocat==========================

        # ===================Calcul Immo==========================
        total_immo = {}
        for immo in immo_price:
            if immo[0] not in total_immo:
                total_immo[immo[0]] = immo[1]
            else:
                total_immo[immo[0]] = total_immo[immo[0]] + immo[1]

        for key, val in total_immo.items():
            result_immo.append([key, val])

        # ===================Calcul Immo==========================

        # ===================Calcul Casino==========================
        total_casino = {}
        for casino in casino_price:
            if casino[0] not in total_casino:
                total_casino[casino[0]] = casino[1]
            else:
                total_casino[casino[0]] = total_casino[casino[0]] + casino[1]

        for key, val in total_casino.items():
            result_casino.append([key, val])

            # ===================Calcul Casino==========================

        # ===================Calcul prime==========================

        result_prime = {}
        for line in prime_entreprise:
            if line[0] in result_prime:
                if line[1] in result_prime[line[0]]:
                    result_prime[line[0]][line[1]] += line[2]
                else:
                    result_prime[line[0]][line[1]] = line[2]

            else:
                result_prime[line[0]] = {}
                result_prime[line[0]][line[1]] = line[2]

        # ===================Calcul prime==========================

        # ===================Calcul Agricole==========================
        total_agricole_price = {}
        for agricole in agricole_price:
            if agricole[0] not in total_agricole_price:
                total_agricole_price[agricole[0]] = agricole[1]
            else:
                total_agricole_price[agricole[0]] = total_agricole_price[agricole[0]] + agricole[1]

        for key, val in total_agricole_price.items():
            result_agricole.append([key, val])

            # ===================Calcul Agricole==========================

        # ===================Calcul Petrol==========================
        total_petrol_quantite = {}
        for petrol in petrol_quantite:
            if petrol[0] not in total_petrol_quantite:
                total_petrol_quantite[petrol[0]] = petrol[1]
            else:
                total_petrol_quantite[petrol[0]] = total_petrol_quantite[petrol[0]] + petrol[1]

        total_petrol_price = {}
        for petrol in petrol_price:
            if petrol[0] not in total_petrol_price:
                total_petrol_price[petrol[0]] = petrol[1]
            else:
                total_petrol_price[petrol[0]] = total_petrol_price[petrol[0]] + petrol[1]

        for key, val in total_petrol_quantite.items():
            result_petrol.append([key, val])

        for petrol in result_petrol:
            petrol.append(round(total_petrol_price[petrol[0]], 2))
        # ===================Calcul Petrol==========================

        # ===================Calcul Electricite==========================
        total_elec_quantite = {}
        for elec in elec_quantite:
            if elec[0] not in total_elec_quantite:
                total_elec_quantite[elec[0]] = elec[1]
            else:
                total_elec_quantite[elec[0]] = total_elec_quantite[elec[0]] + elec[1]

        total_elec_price = {}
        for elec in elec_price:
            if elec[0] not in total_elec_price:
                total_elec_price[elec[0]] = elec[1]
            else:
                total_elec_price[elec[0]] = total_elec_price[elec[0]] + elec[1]

        for key, val in total_elec_quantite.items():
            result_elec.append([key, val])

        for elec in result_elec:
            elec.append(round(total_elec_price[elec[0]], 2))
        # ===================Calcul Electricite==========================

        # ===================Calcul Trading==========================
        total_invest = 0
        total_genere = 0
        total_gain = 0
        for line in trading_investissement:
            pourcentage = 0
            gains = 0
            generation = 0
            investissement = 0
            investissement = round(float(line[-1]), 2)
            total_invest = total_invest + investissement
            for sub_line in trading_pourcentage:
                if line[7] == sub_line[8]:
                    pourcentage = round(float(sub_line[-1]), 2)
            for sub_line in trading_generation:
                if line[7] == sub_line[7]:
                    generation = round(float(sub_line[-1]), 2)
                    total_genere = total_genere + generation
            for sub_line in trading_gains:
                if sub_line[11] in line[7]:
                    gains = round(float(sub_line[6].replace("$", "")), 2)
                    total_gain = total_gain + gains

            result_trading.append(
                ["Entreprise", line[7], "=> Argent investi:", str(investissement) + "$", "Argent généré:",
                 str(generation) + "$", "Gains avec taxe:" + str(gains) + "$", "Pourcentage:" + str(pourcentage) + "%"])
            # ===================Calcul Trading==========================

        # ===================Calcul Warzone==========================
        warzone = Counter(warzone)
        for line in warzone:
            if line.split()[1] == "power":
                if line.split()[0] == "3.0":
                    result_warzone.append(line.split()[3] + " wins " + str(warzone[line] * 3) + " power bonus")
                else:
                    result_warzone.append(line.split()[3] + " wins " + str(warzone[line]) + " power")
            else:
                if line.split()[0] == "180.0":
                    result_warzone.append(line.split()[3] + " wins " + str(warzone[line] * 180) + "$ bonus")
                else:
                    result_warzone.append(line.split()[3] + " wins " + str(warzone[line] * 60) + "$")
        result_warzone.sort()
        # ===================Calcul Warzone==========================

        # ===================Calcul Claim==========================
        unclaim = Counter(unclaim)
        for line in unclaim:
            result_unclaim.append(
                line.split()[0] + " " + line.split()[1] + " a unclaim " + str(unclaim[line]) + " claims du pays " +
                line.split()[2])

        claim = Counter(claim)
        for line in claim:
            result_claim.append(line.split()[0] + " " + line.split()[1] + " a claim " + str(claim[line]) + " fois")

        pillage = Counter(pillage)
        for line in pillage:
            result_pillage.append(
                line.split()[0] + " " + line.split()[1] + " a pillé " + str(pillage[line]) + " claims du pays " +
                line.split()[2])

        surclaim = Counter(surclaim)
        for line in surclaim:
            result_surclaim.append(
                line.split()[0] + " " + line.split()[1] + " a surclaim " + str(surclaim[line]) + " claims du pays " +
                line.split()[2])
        # ===================Calcul Claim==========================

        # ===================Calcul bourse action ==========================
        result_adminshop = {}
        for player, content in itertools.groupby(sorted(adminshop, key=operator.itemgetter(0)),
                                                 key=operator.itemgetter(0)):
            data = list(content)
            result_adminshop[player] = {"amount": sum([x[1] for x in data]), "items": [x[2] for x in data]}
        result_adminshop = OrderedDict(sorted(result_adminshop.items()))
        # ===================Calcul bourse action ==========================

        # ==================Calcul PowerBoost==========================
        c = Counter()
        for name, value in powerboost_joueur:
            c[name] += float(value)

        for line in c:
            result_powerboost_joueur.append([line, str(round(c[line], 2))])

        # ==================Calcul PowerBoost==========================

        # ==================Calcul Enchère==========================
        count = 0
        for line in create_auction:
            if count % 2 == 0:
                sto = line[1] + " a payé " + line[0]
                count = 1
            else:
                sto = sto + " pour créer une enchère de " + line[0] + " " + line[1] + " pour " + line[2] + "$/U"
                result_create_auction.append(sto)
                count = 0

        c = Counter()
        for name, value in augmente_auction:
            c[name] += int(value)

        for line in c:
            if not any(match for match in result_augmente_auction if line.split()[1] in match):
                if c["withdraw " + line.split()[1]] - c["refund " + line.split()[1]] != 0:
                    result_augmente_auction.append(line.split()[1] + " a enchéri de " + str(
                        c["refund " + line.split()[1]]) + "$ et a été remboursé de " + str(
                        c["withdraw " + line.split()[1]]) + "$")

        for line in end_auction:
            if count % 2 == 0:
                sto = line
                count = 1
            else:
                result_end_auction.append(sto + line)
                count = 0
        # ============================================

        pdf.add_page()
        pdf.set_link(page_paiement)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Transfert supérieur à 5000$", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in transfert:
            string = line[0] + " " + line[1] + " " + line[3] + " " + line[7] + " " + line[8] + " " + line[9]
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(90, 4.5, string, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(90, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.add_page()
        pdf.set_link(page_transaction)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Retrait de banque  supérieur à 5000$", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in banque_retrait:
            string = line[0] + " " + line[1] + " " + line[3] + " " + line[4] + " " + str(line[5]) + " " + line[7]
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(90, 4.5, string, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(90, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Dépôt de banque  supérieur à 5000$", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in banque_depot:
            string = line[0] + " " + line[1] + " " + line[3] + " " + line[4] + " " + str(line[5]) + " " + line[7]
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(90, 4.5, string, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(90, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Joueur ayant eu 2 accès dans des banques", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in result_take:
            string = "Joueur " + line[0] + " a accès aux banques " + line[1] + " et " + line[2]
            pdf.cell(40, 5, string, ln=1)
        # ==================Catégorie transaction==========================

        # ==================Catégorie changement de leader==========================
        pdf.add_page()
        pdf.set_link(page_achat)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Pays mise en vente", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in vente:
            string = line[0] + " " + line[1] + " " + line[5] + " " + line[7] + " " + line[9]
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(90, 4.5, string, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(90, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "=============", ln=1)
        pdf.cell(40, 5, "Pays Acheté", ln=1)
        pdf.cell(40, 5, "=============", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in achat:
            string = line[0] + " " + line[1] + " " + line[2] + " " + line[4] + " " + line[5] + " " + line[6] + " " + \
                     line[8]
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(90, 4.5, string, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(90, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "=============", ln=1)
        pdf.cell(40, 5, "Action achetée", ln=1)
        pdf.cell(40, 5, "=============", ln=1)

        pdf.set_font("Arial", size=9)
        for line in achat_action:
            string = ' '.join(line)
            pdf.cell(40, 5, string, ln=1)

        pdf.add_page()
        pdf.set_link(page_leader)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "=============", ln=1)
        pdf.cell(40, 5, "Pays fondés", ln=1)
        pdf.cell(40, 5, "=============", ln=1)

        pdf.set_font("Arial", size=9)
        for line in fondation:
            string = ' '.join(line)
            pdf.cell(40, 5, string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "=============", ln=1)
        pdf.cell(40, 5, "Changement de chef du pays", ln=1)
        pdf.cell(40, 5, "=============", ln=1)

        pdf.set_font("Arial", size=9)
        for line in dirigeant:
            string = line[0] + " " + line[1] + " " + line[5] + " " + line[8] + " " + line[9] + " " + line[12]
            pdf.cell(40, 5, string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Joueur ayant fait une dépense et étant devenu leader", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in transfert:
            if any(line[3] in sublist for sublist in dirigeant):
                string = "Attention à " + line[3] + ": paiement dans la même journée qu'un lead de pays"
                pdf.cell(40, 5, string, ln=1)

        # ==================Catégorie changement de leader==========================

        # ==================Catégorie Notations==========================
        pdf.add_page()
        pdf.set_link(page_notations)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Notations", ln=1)
        pdf.cell(40, 5, "Update lundi à 11h30", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=10)
        pdf.cell(40, 5, "=========Montant total des Notations=========", ln=1)
        pdf.cell(40, 5, "Montant: " + str(notation_global) + "$", ln=1)

        notation.sort(key=lambda x: x[0])
        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in notation:
            if count % 4 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(25, 4.5, row[0], border="TBL")
                pdf.set_xy(35, ybefore)
                pdf.multi_cell(15, 4.5, str(row[1]) + "$", border="TBR")

            elif count % 4 == 1:
                pdf.set_xy(60, ybefore)
                pdf.multi_cell(25, 4.5, row[0], border="TBL")
                pdf.set_xy(85, ybefore)
                pdf.multi_cell(15, 4.5, str(row[1]) + "$", border="TBR")

            elif count % 4 == 2:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(25, 4.5, row[0], border="TBL")
                pdf.set_xy(135, ybefore)
                pdf.multi_cell(15, 4.5, str(row[1]) + "$", border="TBR")

            elif count % 4 == 3:
                pdf.set_xy(160, ybefore)
                pdf.multi_cell(25, 4.5, row[0], border="TBL")
                pdf.set_xy(185, ybefore)
                pdf.multi_cell(15, 4.5, str(row[1]) + "$", border="TBR")

            count += 1

        pdf.add_page()

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Bourse des actions", ln=1)
        pdf.cell(40, 5, "Update lundi à 11h30", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=10)
        pdf.cell(40, 5, "=========Montant total des action=========", ln=1)
        pdf.cell(40, 5, "Montant: " + str(bourse_action_global) + "$", ln=1)

        count = 0
        ybefore = pdf.get_y()
        for row in result_bourse_action:
            pdf.set_font("Arial", size=9)
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(30, 4.5, row, border=1)
                pdf.set_xy(40, ybefore)
                pdf.multi_cell(13, 4.5, str(int(result_bourse_action[row]['amount'])) + "$", border=1)
                pdf.set_xy(53, ybefore)
                pdf.set_font("Arial", size=7)
                pdf.multi_cell(45, 4.5, " ".join(result_bourse_action[row]['country_take']), border=1)

            else:
                pdf.set_xy(103, ybefore)
                pdf.multi_cell(30, 4.5, row, border=1)
                pdf.set_xy(133, ybefore)
                pdf.multi_cell(13, 4.5, str(int(result_bourse_action[row]['amount'])) + "$", border=1)
                pdf.set_xy(146, ybefore)
                pdf.set_font("Arial", size=7)
                pdf.multi_cell(45, 4.5, " ".join(result_bourse_action[row]['country_take']), border=1)
            count += 1
        # ==================Catégorie Notations==========================

        # ==================Catégorie Claim==========================
        pdf.add_page()
        pdf.set_link(page_claim)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Unclaim effectué", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in result_unclaim:
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(90, 4.5, line, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(90, 4.5, line, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Claim effectué", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in result_claim:
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(55, 4.5, line, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(75, ybefore)
                pdf.multi_cell(55, 4.5, line, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            elif count % 3 == 2:
                pdf.set_xy(140, ybefore)
                pdf.multi_cell(55, 4.5, line, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Pillage effectué", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in result_pillage:
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(90, 4.5, line, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(90, 4.5, line, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Surclaim effectué", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for line in result_surclaim:
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(90, 4.5, line, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(90, 4.5, line, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        # ==================Catégorie Claim==========================

        # ==================Catégorie assaut==========================
        pdf.add_page()
        pdf.set_link(page_guerre)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Raison de guerre donnée par le joueur", ln=1)
        pdf.cell(40, 5, "Si le plugin a accepté ou refusé la guerre", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=6)
        for line in result_raison_guerre:
            pdf.cell(40, 5, line, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Raison de guerre donnée par le plugin", ln=1)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.set_font("Arial", size=9)
        for line in plugin_raison_guerre:
            string = ' '.join(line)
            pdf.cell(40, 5, string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Pays ayant débuté une guerre", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in début_guerre:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Pays ayant abandonné une guerre", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in forfait_guerre:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Pays ayant gagné la guerre", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in range(len(guerre_gagnée)):
            if line % 2 == 0:
                reward = guerre_gagnée[line + 1][2:6]
                win = ' '.join(guerre_gagnée[line]) + " " + ' '.join(reward)
                pdf.cell(40, 5, txt=win, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Annulation de guerre", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=10)
        pdf.cell(40, 5, "=========Par le staff=========", ln=1)
        pdf.set_font("Arial", size=9)
        for line in staff_annulation_guerre:
            pdf.cell(40, 5, line, ln=1)

        pdf.set_font("Arial", size=10)
        pdf.cell(40, 5, "=========Par action joueur=========", ln=1)
        pdf.set_font("Arial", size=9)
        for line in joueur_annulation_guerre:
            pdf.cell(40, 5, line, ln=1)

        pdf.set_font("Arial", size=10)
        pdf.cell(40, 5, "=========Par plugin=========", ln=1)
        pdf.set_font("Arial", size=9)
        for line in plugin_annulation_guerre:
            pdf.cell(40, 5, line, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Liste des assauts et missiles", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in assaut:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)
        # ==================Catégorie assaut==========================

        # ==================Catégorie warzone==========================
        pdf.add_page()
        pdf.set_link(page_warzone)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Gains Warzone", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in result_warzone:
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(60, 4.5, row, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(75, ybefore)
                pdf.multi_cell(60, 4.5, row, border="TBLR")

            elif count % 3 == 2:
                pdf.set_xy(140, ybefore)
                pdf.multi_cell(60, 4.5, row, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        # ==================Catégorie warzone==========================

        # ==================Rentrée d'argent==========================
        pdf.add_page()
        pdf.set_link(page_argent)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Argent dépensé dans la météo", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        pdf.cell(40, 5, "météo terrestre: " + str(meteo * 750), ln=1)
        pdf.cell(40, 5, "météo lunaire: " + str(meteo_lunaire * 250), ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Argent dépensé à l'adminshop", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        pdf.cell(40, 5, "Montant global: " + str(adminshop_global), ln=1)

        count = 0
        pdf.set_font("Arial", size=6)
        ybefore = pdf.get_y()
        for row in result_adminshop:
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(20, 4.5, row, border=1)
                pdf.set_xy(30, ybefore)
                pdf.multi_cell(20, 4.5, str(int(result_adminshop[row]['amount'])) + "$", border=1)
                pdf.set_xy(50, ybefore)
                pdf.multi_cell(50, 4.5, " ".join(result_adminshop[row]['items']), border=1)

            else:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(20, 4.5, row, border=1)
                pdf.set_xy(130, ybefore)
                pdf.multi_cell(20, 4.5, str(int(result_adminshop[row]['amount'])) + "$", border=1)
                pdf.set_xy(150, ybefore)
                pdf.multi_cell(50, 4.5, " ".join(result_adminshop[row]['items']), border=1)
                if pdf.get_y() > 276:
                    pdf.add_page()
            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Argent dépensé dans les pub hdv", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        pdf.cell(40, 5, "Montant global: " + str(pub_hdv * 200), ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Argent dépensé pour divorcer", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        pdf.cell(40, 5, "Montant global: " + str(divorce * 750), ln=1)
        # ==================Rentrée d'argent==========================

        # ==================HDV==========================
        pdf.add_page()
        pdf.set_link(page_hdv)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Achat à l'HDV", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=10)
        pdf.cell(40, 5, "=========Montant total des dépenses HDV=========", ln=1)
        pdf.cell(40, 5, "Montant: " + str(hdv) + "$", ln=1)

        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in result_achat_hdv:
            if count % 4 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(35, ybefore)
                pdf.multi_cell(15, 4.5, str(result_achat_hdv[row]) + "$", border="TBR")

            elif count % 4 == 1:
                pdf.set_xy(60, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(85, ybefore)
                pdf.multi_cell(15, 4.5, str(result_achat_hdv[row]) + "$", border="TBR")

            elif count % 4 == 2:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(135, ybefore)
                pdf.multi_cell(15, 4.5, str(result_achat_hdv[row]) + "$", border="TBR")

            elif count % 4 == 3:
                pdf.set_xy(160, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(185, ybefore)
                pdf.multi_cell(15, 4.5, str(result_achat_hdv[row]) + "$", border="TBR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Vente à l'HDV", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in result_vente_hdv:
            if count % 4 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(35, ybefore)
                pdf.multi_cell(15, 4.5, str(result_vente_hdv[row]) + "$", border="TBR")

            elif count % 4 == 1:
                pdf.set_xy(60, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(85, ybefore)
                pdf.multi_cell(15, 4.5, str(result_vente_hdv[row]) + "$", border="TBR")

            elif count % 4 == 2:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(135, ybefore)
                pdf.multi_cell(15, 4.5, str(result_vente_hdv[row]) + "$", border="TBR")

            elif count % 4 == 3:
                pdf.set_xy(160, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(185, ybefore)
                pdf.multi_cell(15, 4.5, str(result_vente_hdv[row]) + "$", border="TBR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1
        # ==================HDV==========================

        # ==================chestshop==========================
        pdf.add_page()
        pdf.set_link(page_chestshop)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Création de ChestShop", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        for line in chestshop:
            string = ' '.join(line)
            if "created" in string:
                pdf.set_font("Arial", size=9)
            else:
                pdf.set_font("Arial", size=6)
            pdf.cell(40, 5, txt=string, ln=1)
        # ==================chestshop==========================

        # ==================Catégorie staff==========================
        pdf.add_page()
        pdf.set_link(page_staff)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "jm effectuée", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in jm:
            string = ' '.join(row)
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(60, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(75, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")


            elif count % 3 == 2:
                pdf.set_xy(140, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")

                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "mutecommerce appliquée", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in mutecommerce:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "mute appliquée", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in mute:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "tempban appliquée", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in tempban:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "He tool demandé", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in he_tool:
            string = ' '.join(row)
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(55, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(70, ybefore)
                pdf.multi_cell(55, 4.5, string, border="TBLR")


            elif count % 3 == 2:
                pdf.set_xy(130, ybefore)
                pdf.multi_cell(55, 4.5, string, border="TBLR")

                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "He search demandé", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in he_search:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)
        # ==================Catégorie staff==========================

        # ==================Catégorie Workstation==========================
        pdf.add_page()
        pdf.set_link(page_tracteur)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Desctruction de tracteur", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in tracteur_detruit:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "spawn de tracteur", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in tracteur_pose:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "craft du tracteur & accessoires", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=6)
        ybefore = pdf.get_y()
        for line in tracteur_donne:
            string = ' '.join(line)
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(60, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(75, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            elif count % 3 == 2:
                pdf.set_xy(140, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "craft des item spéciaux", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=6)
        ybefore = pdf.get_y()
        for line in item_speciaux:
            string = ' '.join(line)
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(60, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(75, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            elif count % 3 == 2:
                pdf.set_xy(140, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "craft des item spacial", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=6)
        ybefore = pdf.get_y()
        for line in item_spatial:
            string = ' '.join(line)
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(60, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(75, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            elif count % 3 == 2:
                pdf.set_xy(140, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "craft des item missiles", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        count = 0
        pdf.set_font("Arial", size=6)
        ybefore = pdf.get_y()
        for line in item_missile:
            string = ' '.join(line)
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(60, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(75, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            elif count % 3 == 2:
                pdf.set_xy(140, ybefore)
                pdf.multi_cell(60, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1
        # ==================Catégorie Workstation==========================

        # ==================Catégorie colonie==========================
        pdf.add_page()
        pdf.set_link(page_colonie)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Demande de colonie", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in colony_demande:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Prélèvement taxe", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in taxe_pays_preleve:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Mise en place de la taxe", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in taxe_pays_define:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)
        # ==================Catégorie colonie==========================

        # ===================Catégorie Entreprise==========================
        pdf.add_page()
        pdf.set_link(page_entreprise)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Création d'entreprise", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in creation_ent:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Injection dans une entreprise", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in injection_ent:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Disband entreprise", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in disband_ent:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Entreprise de trading [Update à 00h00]", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in result_trading:
            string = ' '.join(line)
            pdf.cell(40, 5, txt=string, ln=1)
        pdf.set_font("Arial", size=11)
        pdf.cell(40, 5, txt="Investissement total =" + str(total_invest), ln=1)
        pdf.cell(40, 5, txt="Génération total =" + str(total_genere), ln=1)
        pdf.cell(40, 5, txt="Gain total =" + str(total_gain), ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Entreprise d'électricité", ln=1)
        pdf.set_font("Arial", size=8)
        pdf.set_text_color(220, 20, 60)
        pdf.cell(40, 5, "Rouge: montant 10 fois supérieur à la moyenne", ln=1)
        pdf.set_text_color(255, 140, 0)
        pdf.cell(40, 5, "Orange: montant supérieur à la moyenne", ln=1)
        pdf.set_text_color(34, 139, 34)
        pdf.cell(40, 5, "Vert: montant inférieur ou égal à la moyenne", ln=1)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in result_elec:
            if line[2] > (total_elect / len(result_elec)) * 10:
                pdf.set_text_color(220, 20, 60)
            elif line[2] > total_elect / len(result_elec):
                pdf.set_text_color(255, 140, 0)
            else:
                pdf.set_text_color(34, 139, 34)
            string = line[0] + " Quantité global vendue:" + str(line[1]) + "MW   Argent reçu: " + str(line[2]) + "$"
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Entreprise de pétrole", ln=1)
        pdf.set_font("Arial", size=8)
        pdf.set_text_color(220, 20, 60)
        pdf.cell(40, 5, "Rouge: montant 10 fois supérieur à la moyenne", ln=1)
        pdf.set_text_color(255, 140, 0)
        pdf.cell(40, 5, "Orange: montant supérieur à la moyenne", ln=1)
        pdf.set_text_color(34, 139, 34)
        pdf.cell(40, 5, "Vert: montant inférieur ou égal à la moyenne", ln=1)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in result_petrol:
            if line[2] > (total_petrol / len(result_petrol)) * 10:
                pdf.set_text_color(220, 20, 60)
            elif line[2] > total_petrol / len(result_petrol):
                pdf.set_text_color(255, 140, 0)
            else:
                pdf.set_text_color(34, 139, 34)
            string = line[0] + " Quantité global vendue:" + str(line[1]) + "L   Argent reçu: " + str(line[2]) + "$"
            pdf.cell(40, 5, txt=string, ln=1)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Entreprise d'agricole", ln=1)
        pdf.set_font("Arial", size=8)
        pdf.set_text_color(220, 20, 60)
        pdf.cell(40, 5, "Rouge: montant 10 fois supérieur à la moyenne", ln=1)
        pdf.set_text_color(255, 140, 0)
        pdf.cell(40, 5, "Orange: montant supérieur à la moyenne", ln=1)
        pdf.set_text_color(34, 139, 34)
        pdf.cell(40, 5, "Vert: montant inférieur ou égal à la moyenne", ln=1)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        result_agricole = sorted(result_agricole, key=lambda x: x[0][0])
        count = 0
        ybefore = pdf.get_y()
        for line in result_agricole:
            if line[1] > (total_agricole / len(result_agricole)) * 10:
                pdf.set_text_color(220, 20, 60)
            elif line[1] > total_agricole / len(result_agricole):
                pdf.set_text_color(255, 140, 0)
            else:
                pdf.set_text_color(34, 139, 34)
            string = line[0] + "   Argent reçu: " + str(round(line[1], 2)) + "$"
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(55, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(70, ybefore)
                pdf.multi_cell(55, 4.5, string, border="TBLR")

            elif count % 3 == 2:
                pdf.set_xy(130, ybefore)
                pdf.multi_cell(55, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Entreprise de casino", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        result_casino = sorted(result_casino, key=lambda x: x[0][0])
        count = 0
        ybefore = pdf.get_y()
        for line in result_casino:
            string = line[0] + "   Argent reçu: " + str(round(line[1], 2)) + "$"
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(55, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(70, ybefore)
                pdf.multi_cell(55, 4.5, string, border="TBLR")

            elif count % 3 == 2:
                pdf.set_xy(130, ybefore)
                pdf.multi_cell(55, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Entreprise de location", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        result_immo = sorted(result_immo, key=lambda x: x[0][0])
        count = 0
        ybefore = pdf.get_y()
        for line in result_immo:
            string = line[0] + "   Argent reçu: " + str(round(line[1], 2)) + "$"
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(55, 4.5, string, border="TBLR")

            elif count % 3 == 1:
                pdf.set_xy(70, ybefore)
                pdf.multi_cell(55, 4.5, string, border="TBLR")

            elif count % 3 == 2:
                pdf.set_xy(130, ybefore)
                pdf.multi_cell(55, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

        count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Entreprise d'avocats & pvp", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        for line in result_avocat:
            string = line[0] + "   Argent reçu: " + str(round(line[1], 2)) + "$"
            pdf.cell(40, 5, txt=string, ln=1)
        # ===================Catégorie Entreprise==========================

        # ===================Catégorie prime==========================
        pdf.add_page()
        pdf.set_link(page_prime)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Prime fournies par les entreprises", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        for line in result_prime:
            pdf.set_font("Arial", size=10)
            pdf.cell(40, 5, txt=line + ": ", ln=1)

            pdf.set_font("Arial", size=7)
            count = 0
            ybefore = pdf.get_y()
            total_prime = 0
            for row in result_prime[line]:
                if count % 4 == 0:
                    ybefore = pdf.get_y()
                    pdf.multi_cell(25, 4.5, row, border="TBL")
                    pdf.set_xy(35, ybefore)
                    pdf.multi_cell(15, 4.5, str(result_prime[line][row]) + "$", border="TBR")

                elif count % 4 == 1:
                    pdf.set_xy(55, ybefore)
                    pdf.multi_cell(25, 4.5, row, border="TBL")
                    pdf.set_xy(80, ybefore)
                    pdf.multi_cell(15, 4.5, str(result_prime[line][row]) + "$", border="TBR")

                elif count % 4 == 2:
                    pdf.set_xy(100, ybefore)
                    pdf.multi_cell(25, 4.5, row, border="TBL")
                    pdf.set_xy(125, ybefore)
                    pdf.multi_cell(15, 4.5, str(result_prime[line][row]) + "$", border="TBR")

                elif count % 4 == 3:
                    pdf.set_xy(145, ybefore)
                    pdf.multi_cell(25, 4.5, row, border="TBL")
                    pdf.set_xy(170, ybefore)
                    pdf.multi_cell(15, 4.5, str(result_prime[line][row]) + "$", border="TBR")
                    if pdf.get_y() > 276:
                        pdf.add_page()

                total_prime += result_prime[line][row]
                count += 1
            pdf.set_font("Arial", size=10)
            pdf.cell(40, 5, txt="Total des primes versées pour " + line + ": " + str(total_prime) + "$", ln=1)
            if pdf.get_y() > 276:
                pdf.add_page()
            else:
                pdf.cell(40, 5, txt="-----------------", ln=1)
                # ===================Catégorie prime==========================

        # ===================Catégorie PowerBoost==========================
        pdf.add_page()
        pdf.set_link(page_powerboost)

        pdf.set_font("Arial", size=15)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "PowerBoost", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "PowerBoost pays  [Update à 03h20]", ln=1)
        pdf.cell(40, 5, "PowerBoost à 0 ou perte supérieur à 20", ln=1)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "", ln=1)

        pdf.set_font("Arial", size=9)
        powerboost_pays.sort(key=lambda x: x[0])
        count = 0
        ybefore = pdf.get_y()
        for row in powerboost_pays:
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(35, 4.5, row[0], border=1)
                pdf.set_xy(45, ybefore)
                pdf.multi_cell(10, 4.5, row[1], border="TB")
                pdf.set_xy(55, ybefore)
                pdf.multi_cell(10, 4.5, row[2], border="TBR")

            elif count % 3 == 1:
                pdf.set_xy(70, ybefore)
                pdf.multi_cell(35, 4.5, row[0], border=1)
                pdf.set_xy(105, ybefore)
                pdf.multi_cell(10, 4.5, row[1], border="TB")
                pdf.set_xy(115, ybefore)
                pdf.multi_cell(10, 4.5, row[2], border="TBR")

            elif count % 3 == 2:
                pdf.set_xy(130, ybefore)
                pdf.multi_cell(35, 4.5, row[0], border=1)
                pdf.set_xy(165, ybefore)
                pdf.multi_cell(10, 4.5, row[1], border="TB")
                pdf.set_xy(175, ybefore)
                pdf.multi_cell(10, 4.5, row[2], border="TBR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "PowerBoost joueur", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        count = 0
        ybefore = pdf.get_y()
        for line in result_powerboost_joueur:
            if count % 4 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(25, 4.5, line[0], border="TBL")
                pdf.set_xy(35, ybefore)
                pdf.multi_cell(15, 4.5, "+ " + str(line[1]), border="TBR")

            elif count % 4 == 1:
                pdf.set_xy(60, ybefore)
                pdf.multi_cell(25, 4.5, line[0], border="TBL")
                pdf.set_xy(85, ybefore)
                pdf.multi_cell(15, 4.5, "+ " + str(line[1]), border="TBR")

            elif count % 4 == 2:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(25, 4.5, line[0], border="TBL")
                pdf.set_xy(135, ybefore)
                pdf.multi_cell(15, 4.5, "+ " + str(line[1]), border="TBR")

            elif count % 4 == 3:
                pdf.set_xy(160, ybefore)
                pdf.multi_cell(25, 4.5, line[0], border="TBL")
                pdf.set_xy(185, ybefore)
                pdf.multi_cell(15, 4.5, "+ " + str(line[1]), border="TBR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        # ===================Catégorie PowerBoost==========================

        # ===================Catégorie enchères==========================
        pdf.add_page()
        pdf.set_link(page_enchere)

        pdf.set_font("Arial", size=15)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Les enchères", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Création d'enchères", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        result_create_auction.sort(key=lambda x: x[0])
        for line in result_create_auction:
            pdf.cell(40, 5, line, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Enchérissement", ln=1)
        pdf.cell(40, 5, "Si la somme enchérie et remboursée n'est pas égal", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        result_augmente_auction.sort(key=lambda x: x[0])
        for line in result_augmente_auction:
            pdf.cell(40, 5, line, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Enchère terminée", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        result_end_auction.sort(key=lambda x: x[0])
        for line in result_end_auction:
            pdf.cell(40, 5, line, ln=1)

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Enchère annulée", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        remove_auction.sort(key=lambda x: x[0])
        for line in remove_auction:
            pdf.cell(40, 5, line, ln=1)

        # ===================Catégorie enchères==========================

        # ===================Catégorie Mort==========================

        # ===================Catégorie Mort==========================
        pdf.add_page()
        pdf.set_link(page_deaths)
        pdf.set_font("Arial", size=15)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Les morts", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=4)
        count = 0
        ybefore = pdf.get_y()
        for line in death:
            line = ' '.join(line)
            if count % 3 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(60, 4.5, line, border="TBL")

            elif count % 3 == 1:
                pdf.set_xy(70, ybefore)
                pdf.multi_cell(60, 4.5, line, border="TBRL")

            elif count % 3 == 2:
                pdf.set_xy(130, ybefore)
                pdf.multi_cell(60, 4.5, line, border="TBR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1
            # ===================Catégorie Mort==========================

        # ==================Duel==========================
        pdf.add_page()
        pdf.set_link(page_duel)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Gagant duel", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=10)
        pdf.cell(40, 5, "=========Montant total des gains due=========", ln=1)
        pdf.cell(40, 5, "Montant: " + str(duel_amount) + "$", ln=1)

        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in result_duel_win:
            if count % 4 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(35, ybefore)
                pdf.multi_cell(15, 4.5, str(result_duel_win[row]) + "$", border="TBR")

            elif count % 4 == 1:
                pdf.set_xy(60, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(85, ybefore)
                pdf.multi_cell(15, 4.5, str(result_duel_win[row]) + "$", border="TBR")

            elif count % 4 == 2:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(135, ybefore)
                pdf.multi_cell(15, 4.5, str(result_duel_win[row]) + "$", border="TBR")

            elif count % 4 == 3:
                pdf.set_xy(160, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(185, ybefore)
                pdf.multi_cell(15, 4.5, str(result_duel_win[row]) + "$", border="TBR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Perte en duel", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in result_duel_loose:
            if count % 4 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(35, ybefore)
                pdf.multi_cell(15, 4.5, str(result_duel_loose[row]) + "$", border="TBR")

            elif count % 4 == 1:
                pdf.set_xy(60, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(85, ybefore)
                pdf.multi_cell(15, 4.5, str(result_duel_loose[row]) + "$", border="TBR")

            elif count % 4 == 2:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(135, ybefore)
                pdf.multi_cell(15, 4.5, str(result_duel_loose[row]) + "$", border="TBR")

            elif count % 4 == 3:
                pdf.set_xy(160, ybefore)
                pdf.multi_cell(25, 4.5, row, border="TBL")
                pdf.set_xy(185, ybefore)
                pdf.multi_cell(15, 4.5, str(result_duel_loose[row]) + "$", border="TBR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1
        # ==================Duel==========================

        # ==================minerais obscur et bois==========================
        pdf.add_page()
        pdf.set_link(page_obscur)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Minerais obscur", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        magnesium = 0
        gallium = 0
        nobium = 0
        total_obscur = 0
        total_bois = 0
        for line in minerais_bois:
            pdf.set_font("Arial", size=10)
            pdf.cell(40, 5, txt=line + ": ", ln=1)

            pdf.set_font("Arial", size=8)
            ybefore = pdf.get_y()

            try:
                pdf.multi_cell(25, 4.5, "Magnésium : " + str(minerais_bois[line]["MAGNESIUM"]), border="TBLR")
                magnesium += minerais_bois[line]["MAGNESIUM"]
            except:
                pdf.multi_cell(25, 4.5, "Magnésium : 0", border="TBLR")
                pass

            pdf.set_xy(35, ybefore)
            try:
                pdf.multi_cell(25, 4.5, "Gallium : " + str(minerais_bois[line]["GALLIUM"]), border="TBLR")
                gallium += minerais_bois[line]["GALLIUM"]
            except:
                pdf.multi_cell(25, 4.5, "Gallium : 0", border="TBLR")
                pass

            pdf.set_xy(60, ybefore)
            try:
                pdf.multi_cell(25, 4.5, "Niobium : " + str(minerais_bois[line]["NIOBIUM"]), border="TBLR")
                nobium += minerais_bois[line]["NIOBIUM"]
            except:
                pdf.multi_cell(25, 4.5, "Niobium : 0", border="TBLR")
                pass

            pdf.set_xy(85, ybefore)
            try:
                pdf.multi_cell(30, 4.5, "Minerais spawn : " + str(minerais_bois[line]["obscur"]), border="TBLR")
                total_obscur += minerais_bois[line]["obscur"]
            except:
                pdf.multi_cell(30, 4.5, "Minerais spawn : 0", border="TBLR")
                pass

            pdf.set_xy(115, ybefore)
            try:
                pdf.multi_cell(30, 4.5, "Bois spawn : " + str(minerais_bois[line]["bois"]), border="TBLR")
                total_bois += minerais_bois[line]["bois"]
            except:
                pdf.multi_cell(30, 4.5, "Bois spawn : 0", border="TBLR")
                pass

            pdf.cell(40, 5, txt="-----------------", ln=1)
        if pdf.get_y() > 276:
            pdf.add_page()

        pdf.set_font("Arial", size=10)
        pdf.cell(40, 5, txt="Total des magnésium minés " + str(magnesium), ln=1)
        pdf.cell(40, 5, txt="Total des gallium minés " + str(gallium), ln=1)
        pdf.cell(40, 5, txt="Total des nobium minés " + str(nobium), ln=1)
        pdf.cell(40, 5, txt="Total des minerais spawn " + str(total_obscur), ln=1)
        pdf.cell(40, 5, txt="Total bois spawn " + str(total_bois), ln=1)

        # ==================Access==========================

        pdf.add_page()
        pdf.set_link(page_access)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Les accès", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=9)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Les give d'accès", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=7)
        count = 0
        ybefore = pdf.get_y()
        for row in access_player_true:
            string = ' '.join(row)
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(80, 4.5, string, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(100, ybefore)
                pdf.multi_cell(80, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        pdf.set_font("Arial", size=9)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Les retrait d'accès", ln=1)
        pdf.cell(40, 5, "==================", ln=1)
        count = 0
        pdf.set_font("Arial", size=7)
        ybefore = pdf.get_y()
        for row in access_player_false:
            string = ' '.join(row)
            if count % 2 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(80, 4.5, string, border="TBLR")

            elif count % 2 == 1:
                pdf.set_xy(100, ybefore)
                pdf.multi_cell(80, 4.5, string, border="TBLR")
                if pdf.get_y() > 276:
                    pdf.add_page()

            count += 1

        # =======================Meteor==================
        pdf.add_page()
        pdf.set_link(page_meteore)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 5, "==================", ln=1)
        pdf.cell(40, 5, "Les météores", ln=1)
        pdf.cell(40, 5, "==================", ln=1)

        pdf.set_font("Arial", size=5)
        count = 0
        ybefore = pdf.get_y()
        for row in meteore:
            if "WORLD" in row:
                pdf.set_text_color(34, 139, 34)
            elif "MARS" in row:
                pdf.set_text_color(255, 140, 0)
            else:
                pdf.set_text_color(169, 169, 169)

            if count % 4 == 0:
                ybefore = pdf.get_y()
                pdf.multi_cell(40, 4.5, row, border="TBLR")

            elif count % 4 == 1:
                pdf.set_xy(60, ybefore)
                pdf.multi_cell(40, 4.5, row, border="TBLR")

            elif count % 4 == 2:
                pdf.set_xy(110, ybefore)
                pdf.multi_cell(40, 4.5, row, border="TBLR")

            elif count % 4 == 3:
                pdf.set_xy(160, ybefore)
                pdf.multi_cell(40, 4.5, row, border="TBLR")

                if pdf.get_y() > 276:
                    pdf.set_text_color(0, 0, 0)
                    pdf.add_page()

            count += 1

        pdf.output(path+"/pdf/red-"+os.path.basename(file).split('.')[0]+".pdf","F")
    print(file+" converti !")
print("Fin du programme")