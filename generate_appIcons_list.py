
import random

# provide below data from your project and run code 

names = [
   'tools_clamp_clamps_tool_construction_diy',
'tools_chainsaw_gardening_construction_tool_1',
'tools_brush_paint_tool',
'tools_adjustable_spanner_wrench_tool_construction',
'supermarket_shopping_cart_trolley_caddy_ecommerce',
'supermarket_shopping_bag_paper_grocery_groceries',
'supermarket_flower_flowers_shop_store',
'supermarket_bag_shopping_buy_ecommerce_online',
'sport_weight_training_weights_dumbbel_fitness_sport',
'sport_soccer_football_shoes_cleats',
'sport_ski_skier_winter_sport',
'sport_ping_pong_tennis_table',
'sport_ice_skating_skates_shoes',
'sport_exercise_bike_apartment_hometrainer',
'sport_boxing_glove_gloves_sport',
'sport_basketball_hoop_basket_sport',
'sport_ball_balloon_beach_game',
'sport_badminton_shuttlecock_game_sport',
'others_worker_builder_construction_2',
'others_pie_chart_statistics_diagram_graph',
'others_no_smoking_area_sign_hotel_2',
'others_infographic_chart_graph_statistics_business_1',
'others_heart_hands_care_healthcare_medicine_medical_1',
'others_gift_present_offer_give_1',
'others_gift_card_coupon_give_offer_1',
'others_cloud_upload_storage_backup',
'others_cloud_download',
'others_add_new_plus_2',
'office_note_it_post_pin',
'office_letter_enveloppe_message_mail',
'office_document_stopwatch_timer_training',
'office_document_file_text_business',
'office_cash_register_shopping_finance',
'office_building_office_company_real_estate',
'office_briefcase_suitcase_portfolio_business_office',
'office_binders_files_office_business',
'office_badge_id_card_identification',
'office_balance_finance_money_scales',
'medicine_uterus_gynecology_medical_medicine_healthcare',
'medicine_vaccine_syringe_injection_medical',
'medicine_stethoscope_doctor_cardiology_medical_medicine',
'medicine_pregnant_embryo_fetus_baby',
'medicine_microscope_laboratory_research_medical_science_medicine',
'medicine_medical_nurse_woman_medecine_healthcare',
'medicine_kidney_organ_anatomy_medicine_medical',
'medicine_herbal_medicine_phytotherapy_plant_traditional_healthcare_1',
'medicine_heart_human_organ_medicine_medical_healthcare',
'medicine_drip_intravenous_infusion_saline_transfusion_medical_medicine',
'medicine_brain_neuron_intelligence_mind_medical_medicine',
'medicine_bottle_pills_medicine_medical_drugs_prescription',
'medicine_bottle_pills_medical_medicine_drugs_prescription',
'medicine_bacteria_virus_disease_germs_medical_microbe_medicine',
'medicine_ambulance_emergency_medicine_medical_hospital',
'home_shield_check_security_protection',
'home_surveillance_camera_security_cctv',
'home_plumbing_tap_faucet_water_leak',
'home_lightbulb_led_ecological_ecology_eco',
'home_light_bulb_idea_business',
'home_hotel_shower_bathroom_service',
'home_flower_pot_gardening_floral',
'home_ecology_eco_house_home_green',
'home_bath_bathtub_bathroom',
'home_air_conditioning_conditioner_house_home_real_estate',
'helthcare_tooth_brush_toothbrush_paste_healthcare_hygiene',
'helthcare_toilet_paper_roll_wipe_clean_1',
'helthcare_tablet_website_online_app_medical_medicine',
'helthcare_syrup_bottle_spoon_medicine_medical_healthcare_1',
'helthcare_sun_cream_sunscreen_lotion_protection',
'helthcare_spray_sprayer_clean_cleaning_1',
'helthcare_liquid_soap_wash_clean',
'helthcare_laundry_wash_hand_cleaning_washing',
'helthcare_laundry_detergent_liquid_wash',
'helthcare_herbal_medicine_phytotherapy_plant_healthcare_traditional',
'furniture_washing_machine_laundry_cleaning',
'furniture_wash_clean_dishes_dish_plates',
'furniture_toaster_toast_bread_kitchen_appliance',
'furniture_television_tv_hotel_1',
'furniture_refrigerator_fridge_kitchen',
'furniture_lockers_room_school_university_gym',
'furniture_kitchen_interior_furniture_1',
'furniture_italian_coffee_maker',
'furniture_electric_mixer_hand_blender_beater',
'furniture_cutting_board_cut_knife_kitchen',
'furniture_blender_juice_mixer_kitchen_appliance',
'furniture_armchair_lounge_living_room_hotel',
'furniture_armchair_chair_office_business',
'food_wine_white_glass_drink',
'food_wine_red_white_bottle_glass',
'food_tomato_fruit_vegetable_food',
'food_steak_beef_meat_food',
'food_shrimp_seafood_prawn_food_1',
'food_sausage_food_bbq_barbecue',
'food_sandwich_meal_lunch_fast_food',
'food_salmon_fish_grill_food_steak',
'food_pizza_cutter_cut_kitchen_utensil',
'food_pineapple_fruit_food',
'food_pills_herbal_medicine_phytotherapy_plant_medical_drugs_1',
'food_milk_bottle_drink_1',
'food_ice_cream_icecream_cone',
'food_hamburger_burger_fastfood',
'food_fish_seafood_food',
'food_eggplant_vegetable_food',
'food_egg_boiled_food_cup',
'food_donut_doughnut_sweet_pastry',
'food_coffee_cup_drink',
'food_coffee_cup',
'food_chicken_grilled_leg_drumstick_1',
'food_carrot_vegetable_food',
'food_bread_loaf_bakery_food',
'food_blackberry_raspberry_berry_fruit_food',
'food_banana_fruit_food',
'food_acorn_hazelnut_nut_autumn_1',
'finance_wallet_cash_money_payment_buy_shopping',
'finance_suitcase_briefcase_cash_dollar_money',
'finance_statistics_increase_graph_success',
'finance_statistics_decrease_graph_falling',
'finance_statistics_analysis_graph_mobile_phone',
'finance_safe_robbery_holdup_bank',
'finance_safe_bank_vault_security',
'finance_piggy_bank_savings_save',
'finance_phone_call_talk_money_dollar',
'finance_objective_target_financial_goal_goals',
'finance_money_cash_dollars_dollar',
'finance_money_bribe_dollars_corruption_cash',
'finance_magnifier_search_money_dollar_business',
'finance_letter_enveloppe_dollar_payment_money',
'finance_international_finance_business_economy',
'finance_dollar_hands_business_exchange',
'finance_currency_conversion_exchange_money',
'finance_credit_card_payment_online_shopping_buy',
'finance_credit_card_machine_pay_payment',
'finance_credit_card_buy_shopping_payment',
'finance_conference_meeting_presentation_business_finance',
'finance_check_finance_bank_business_payment',
'finance_bribe_dollars_corruption_money_pay',
'family_teddy_bear_toy_baby',
'family_stroller_baby_pram_carriage',
'family_rose_love_romantic_valentine_s_day_flower',
'family_rattle_baby_toy',
'family_pregnant_embryo_fetus_baby',
'family_plastic_duck_toy_bath',
'family_pacifier_baby_dummy_child',
'family_heterosexual_couple_sexuality_love',
'family_gift_heart_love_valentine_day',
'family_flowers_bouquet_love_valentine_s_day',
'family_engagement_ring_box_jewel_diamond_wedding',
'family_dog_pet_allowed_friendly_1',
'family_deck_sun_chair_umbrella_beach_lounger',
'family_christmas_tree_xmas',
'family_candle_romantic_love_date_valentine_s_day',
'family_baby_mobile_toy',
'family_baby_child_kid_girl',
'family_baby_bottle_milk',
'entertainement_surf_surfboard_surfing_board_sport',
'entertainement_skateboard_skate_skateboarding_board',
'entertainement_skateboard_skate_board_skateboarding',
'entertainement_rollerblade_roller_skates_skating',
'entertainement_parachute_jumping_parachutist_jump_skydiving',
'entertainement_joystick_game_controller_pad',
'entertainement_jet_ski_jetski_sport',
'entertainement_fishing_fish_float_sport',
'entertainement_chess_game_horse',
'entertainement_casino_poker_card_cards_game_gambling',
'entertainement_bowling_ball_game',
'entertainement_ace_heart_card_game',
'electronic_telephone_phone_call',
'electronic_smartphone_phone_mobile_cell',
'electronic_smart_watch_smartwatch',
'electronic_printer_inkjet_print_fax_scanner',
'electronic_ear_defenders_hearing_protection_tool_headphones',
'electronic_camera_photo_photography_digital',
'electronic_cable_usb_adapter_connector_1',
'education_pie_chart_graph_laptop_computer_business',
'education_painting_palette_paint_brush_art',
'education_movie_video_window_application_player',
'education_guitar_accoustic_instrument_music',
'education_graduation_hat_cap_graduate_university',
'education_computer_atom_electron_molecule_science_research',
'education_calculator_accounting_math',
'education_book_school_education_knowledge',
'education_book_books_education_library_school_knowledge',
'communication_website_web_site_page_internet',
'communication_tablet_touchscreen_application_apps_device',
'communication_sim_card_mobile_1',
'communication_router_modem_wifi_network',
'communication_computer_keyboard_wireless_wifi',
'communication_businessman_teamwork_network_partnership_connection_team_business',
'communication_businessman_network_management_strategy_connection_people_business',
'communication_blog_website_webpage_web_internet',
'clothes_tie_business_office',
'clothes_shirt_dry_cleaning_clothes_laundry',
'clothes_cheongsam_chinese_dress_gown_mandarin_svgrepo_com',
'clothes_ballerina_dance_shoes_slippers',
'clothes_babydoll_lingerie_nightie_sexy',
'beauty_style_perfume_love_heart_valentine_s_day',
'beauty_style_ointment_cream_medicine_healthcare_health_medical_1',
'beauty_style_lipstick_makeup_cosmetic_beauty',
'beauty_style_dermatology_hair_roots_skin_transplant_medical',
'travel_travel_destination_trip_location_hotel',
'travel_postcard_photos_sunset_travel',
'travel_luggage_suitcase_travel',
'travel_flight_travel_business_trip',
'travel_caravan_camping_trailer_vacation_travel',
'travel_car_vacation_travel_summer_trip',
'travel_backpack_camping_travel_bag',
'transportation_taxi_cab_hotel_service_transport',
'transportation_parking_sign_area_hotel_service',
'transportation_oil_barrel_petroleum_1',
'transportation_motorcycle_helmet_race_safety',
'transportation_fuel_gas_pump_petrol_ecology_green_eco',
'transportation_freight_train_goods_shipping_logistics',
'transportation_fast_delivery_truck_logistics_shipping',
'transportation_delivery_truck_fast_shipping',
'transportation_cargo_ship_freighter_shipping_logistics',
'transportation_camping_car_van_bus_minibus',
'transportation_bike_bicycle_cycling_sport',
'transportation_airplane_plane_logistics_delivery_shipping',
'tools_pliers_tool_construction_equipment',
'app_icons_icon3',
'app_icons_settings_controls_configuration_preferences_sliders',
'app_icons_pen_edit_pencil_write_writing',
'app_icons_calendar_date_schedule_appointment',
]
code_points = [
   0xe800,
0xe801,
0xe802,
0xe804,
0xe805,
0xe806,
0xe807,
0xe809,
0xe80a,
0xe80b,
0xe80c,
0xe80d,
0xe80e,
0xe80f,
0xe810,
0xe811,
0xe813,
0xe814,
0xe815,
0xe816,
0xe818,
0xe819,
0xe81a,
0xe81b,
0xe81c,
0xe81d,
0xe81e,
0xe81f,
0xe823,
0xe824,
0xe825,
0xe826,
0xe828,
0xe829,
0xe82a,
0xe82b,
0xe82c,
0xe82d,
0xe82f,
0xe830,
0xe832,
0xe833,
0xe834,
0xe835,
0xe837,
0xe838,
0xe83a,
0xe83b,
0xe83c,
0xe83d,
0xe83e,
0xe83f,
0xe840,
0xe843,
0xe844,
0xe845,
0xe846,
0xe847,
0xe848,
0xe84a,
0xe84b,
0xe84c,
0xe84d,
0xe84e,
0xe84f,
0xe850,
0xe851,
0xe852,
0xe853,
0xe854,
0xe855,
0xe856,
0xe857,
0xe859,
0xe85a,
0xe85b,
0xe85c,
0xe85d,
0xe85e,
0xe85f,
0xe860,
0xe862,
0xe863,
0xe865,
0xe866,
0xe867,
0xe868,
0xe869,
0xe86a,
0xe86b,
0xe86c,
0xe86d,
0xe86e,
0xe86f,
0xe870,
0xe871,
0xe872,
0xe873,
0xe874,
0xe875,
0xe876,
0xe877,
0xe878,
0xe879,
0xe87b,
0xe87c,
0xe87d,
0xe87f,
0xe880,
0xe881,
0xe882,
0xe884,
0xe885,
0xe886,
0xe887,
0xe888,
0xe889,
0xe88a,
0xe88b,
0xe88c,
0xe88d,
0xe88e,
0xe88f,
0xe890,
0xe891,
0xe892,
0xe893,
0xe894,
0xe895,
0xe896,
0xe897,
0xe898,
0xe899,
0xe89a,
0xe89b,
0xe89c,
0xe89d,
0xe89e,
0xe89f,
0xe8a0,
0xe8a1,
0xe8a3,
0xe8a6,
0xe8a7,
0xe8a8,
0xe8a9,
0xe8aa,
0xe8ab,
0xe8ad,
0xe8ae,
0xe8af,
0xe8b0,
0xe8b1,
0xe8b3,
0xe8b5,
0xe8b6,
0xe8b7,
0xe8b8,
0xe8b9,
0xe8ba,
0xe8bb,
0xe8bc,
0xe8bd,
0xe8be,
0xe8bf,
0xe8c0,
0xe8c1,
0xe8c2,
0xe8c3,
0xe8c5,
0xe8c6,
0xe8c7,
0xe8c8,
0xe8c9,
0xe8ca,
0xe8cb,
0xe8cc,
0xe8ce,
0xe8cf,
0xe8d0,
0xe8d1,
0xe8d3,
0xe8d4,
0xe8d5,
0xe8d6,
0xe8d9,
0xe8da,
0xe8db,
0xe8dc,
0xe8dd,
0xe8df,
0xe8e0,
0xe8e2,
0xe8e3,
0xe8e4,
0xe8e5,
0xe8e6,
0xe8e8,
0xe8e9,
0xe8ea,
0xe8eb,
0xe8ec,
0xe8ed,
0xe8ee,
0xe8ef,
0xe8f0,
0xe8f1,
0xe8f2,
0xe8f3,
0xe8f4,
0xe8f5,
0xe8f6,
0xe8f7,
0xe8f8,
0xe8fa,
0xe8fb,
0xe8fc,
0xe8fd,
0xe902,
0xe908,
0xe90a,
0xe90b,
]
colors_name = [
   'lightPurple',
   'lightBlue',
   'amber',
   'lightGreen',
   'blueGreen',
   'cyan',
   'pink',
   'lightRed'
]
N = len(names);



# print('final List<AppIcon> appIcons = <AppIcon>[')
for i in range(100,N):
   print('  AppIcon(')
   print(f'    id: {i+1},')
   print(f"    name: '{names[i]}',")
   print(f'    codePoint:{code_points[i]},')
   print(f'    bgColor: IconBackgroundColors.{random.choice(colors_name)}.value & 0xFFFFFFFF,')
   print('    textColor: 0xFFFFFFFF,')
   print('    iconCategoryId: xxx ,')
   print('  ),')


# print(']')