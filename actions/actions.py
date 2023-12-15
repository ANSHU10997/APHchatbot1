from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hey, I am FusionWizz, How can I help you?")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bye, have a nice day.")
        return []

class ActionBotChallenge(Action):
    def name(self) -> Text:
        return "utter_bot_challenge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sorry, Please ask me questions regarding APH Approval Process Handbook")
        return []

class ActionGeneralInfoVocationalEducation(Action):
    def name(self) -> Text:
        return "utter_general_info_vocational_education"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Vocational Education is occupation-based learning with practical training, directly developing expertise in specific skills. It differs from traditional education by focusing on job preparation and skill specialization.")
        return []

class ActionNSQF(Action):
    def name(self) -> Text:
        return "utter_nsqf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="NSQF is a competency-based framework organizing qualifications into levels (1 to 10) based on knowledge, skills, and aptitude. It applies to formal, non-formal, or informal learning and ensures learners possess defined outcomes.")
        return []

class ActionAffiliationVocationalCourses(Action):
    def name(self) -> Text:
        return "utter_affiliation_vocational_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Vocational Courses may affiliate with existing universities, Skill Universities, or National Universities. Affiliation can also be with the Board of Technical Education, depending on the circumstances.")
        return []

class ActionDVocBVocProgrammes(Action):
    def name(self) -> Text:
        return "utter_d_voc_b_voc_programmes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="These programs provide Diploma/Undergraduate studies integrating specific job roles and their Qualification Packs/National Occupational Standards, along with a foundation in general education.")
        return []

class ActionRegulationFeesVocationalCourses(Action):
    def name(self) -> Text:
        return "utter_regulation_fees_vocational_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The fees for Vocational Courses are regulated by respective state bodies, Technical Boards, Universities, or relevant authorities depending on the jurisdiction.")
        return []

class ActionCreditBasedModularPrograms(Action):
    def name(self) -> Text:
        return "utter_credit_based_modular_programs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Modular programs have credits for skill and general education, allowing multiple exits and entries. Learners can seek employment after any award level and return to upgrade skills or qualifications as needed.")
        return []

class ActionCurriculumMixVocationalEducation(Action):
    def name(self) -> Text:
        return "utter_curriculum_mix_vocational_education"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The curriculum should have a suitable mix with 40% of total credits allocated to general education and the remaining 60% to skill development components.")
        return []

class ActionCurriculumApprovalOversight(Action):
    def name(self) -> Text:
        return "utter_curriculum_approval_oversight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The curriculum details are approved by respective Technical Boards or Universities. Oversight is conducted by the Ministry of Education (MoE) or relevant authorities.")
        return []

class ActionRoleGeneralEducationComponent(Action):
    def name(self) -> Text:
        return "utter_role_general_education_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The General Education Component constitutes 40% of total credits, providing a balanced educational foundation alongside the specialized skill development components.")
        return []

class ActionEmphasisCreditBasedModularPrograms(Action):
    def name(self) -> Text:
        return "utter_emphasis_credit_based_modular_programs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Credit-based modular programs allow flexibility for learners, enabling them to enter the workforce at various award levels and return to upgrade qualifications or skills as needed.")
        return []

class ActionFocusSkillDevelopmentComponentDesign(Action):
    def name(self) -> Text:
        return "utter_focus_skill_development_component_design"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The skill development component should lead to comprehensive specialization in one or two domains, ensuring a thorough understanding of the selected job roles.")
        return []

class ActionNationalOccupationalStandards(Action):
    def name(self) -> Text:
        return "utter_national_occupational_standards"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="In such cases, the university/college should collaborate with industry experts to develop the curriculum for the specific area or job role.")
        return []

class ActionCurriculumEmphasisWorkReadinessSkills(Action):
    def name(self) -> Text:
        return "utter_curriculum_emphasis_work_readiness_skills"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The curriculum should focus on developing work-ready skills in each of the three years, including practical work, on-the-job training, student portfolios, and project work.")
        return []

class ActionDeterminingGeneralEducationComponent(Action):
    def name(self) -> Text:
        return "utter_determining_general_education_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The Board of Studies of the affiliating University/Board decides the general education component, adhering to normal university standards. It includes holistic development courses, support to core trade, soft skills, IT skills, and language proficiency.")
        return []

class ActionCompletingSkillModulesAcquiringCredits(Action):
    def name(self) -> Text:
        return "utter_completing_skill_modules_acquiring_credits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Students complete skill modules at various certification levels, acquiring necessary credits from Skill Knowledge Providers (SKP), Training Providers, or Sector Skill Councils approved by NSDC or relevant authorities.")
        return []

class ActionCreditTransferCertification(Action):
    def name(self) -> Text:
        return "utter_credit_transfer_certification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Credits, including skill and education components, are transferred to the Technical Board or University. If the required credits for a certification level are met, the Technical Board or University awards the certification.")
        return []

class ActionCertificationLevelsInformation(Action):
    def name(self) -> Text:
        return "utter_certification_levels_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="All certification levels are identified in Appendix 1 of the document. Specific details can be referred to in the SAMVAY Document accessible at: SAMVAY Document.")
        return []

class ActionGeneralStreamToVocationalStreamTransition(Action):
    def name(self) -> Text:
        return "utter_general_stream_to_vocational_stream_transition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="A student can enter at a certain level, provided the required skills are acquired from a registered SKP/Training Provider. Institutions may offer bridge courses for necessary knowledge transfer for those seeking lateral entry.")
        return []

class ActionMovementBetweenVocationalAndFormalHigherEducationStreams(Action):
    def name(self) -> Text:
        return "utter_movement_between_vocational_and_formal_higher_education_streams"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Candidates have the freedom to move between Vocational and formal higher education streams at various stages, including multi-level entry and exit systems, subject to fulfilling the required criteria of the affiliating body.")
        return []

class ActionNOCProcess(Action):
    def name(self) -> Text:
        return "utter_noc_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The institution must apply online on the AICTE Web-Portal as per the calendar of AICTE for seeking NOC (No Objection Certificate).")
        return []

class ActionPrerequisitesForEstablishingTechnicalInstitution(Action):
    def name(self) -> Text:
        return "utter_prerequisites_for_establishing_technical_institution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The new technical institution should meet the infrastructure requirements outlined in the Approval Process Handbook. Additionally, it should have prior approval from the Council before offering any technical courses.")
        return []

class ActionSignificanceOfAdheringToLaws(Action):
    def name(self) -> Text:
        return "utter_significance_of_adhering_to_laws"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The institution must adhere to existing Central, State, and Local Laws, along with norms from other Regulatory Bodies if applicable, in order to ensure compliance and legality in its establishment and operation.")
        return []

class ActionRoleOfStateGovernmentInEstablishment(Action):
    def name(self) -> Text:
        return "utter_role_of_state_government_in_establishment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The State Government/UT is expected to provide financial assistance for the establishment of technical institutions offering engineering and technology programs at DIPLOMA/UG/PG levels. The government should have a budget provision of at least ₹100 lakh and provide the necessary land.")
        return []

class ActionAICTEHandlingApplications(Action):
    def name(self) -> Text:
        return "utter_AICTE_handling_applications"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("AICTE notifies the application process through Public Notices and its website, setting cut-off dates for various categories. The application process is conducted online through the AICTE Web Portal using the National Single Window System (NSWS). Offline applications are not accepted.")
        return []

class ActionTimeFrameForSubmissionAndConsequences(Action):
    def name(self) -> Text:
        return "utter_time_frame_for_submission_and_consequences"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("AICTE specifies a time schedule through Public Notices and its website for the submission of applications. It is mandatory for applications to be submitted on the AICTE Web Portal through NSWS, with both the application and payment made by the last date as notified in the Public Notice/AICTE Website. Applications submitted after the deadline will not be accepted.")
        return []

class ActionTypesOfProgramsForApproval(Action):
    def name(self) -> Text:
        return "utter_types_of_programs_for_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("A new technical institution can seek approval to offer programs in Engineering and Technology, Planning, Applied Arts and Crafts, Design, Hotel Management and Catering Technology (Diploma/Undergraduate Degree Level), Computer Application (MCA), and Management (Post Graduate Certificate/Post Graduate Diploma/Post Graduate Degree Level).")
        return []

class ActionEligibilityCriteriaForPromoters(Action):
    def name(self) -> Text:
        return "utter_eligibility_criteria_for_promoters"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Promoters can be a Society registered under the Societies Registration Act, 1860, a Trust registered under the Indian Trust Act, 1882, a Company established under Section 8 of the Companies Act, 2013, or the Central/State Government/UT Administration. Foreign equity in a company applying for the establishment of a technical institution is generally not permitted.")
        return []

class ActionIneligibilityOfCertainPrograms(Action):
    def name(self) -> Text:
        return "utter_ineligibility_of_certain_programs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("New institutions are not eligible for these programs as per section 1.3.3. The specific reasons for this exclusion are not provided in the given content.")
        return []

class ActionMinistryOfEducationSchemesForEstablishment(Action):
    def name(self) -> Text:
        return "utter_Ministry_of_Education_schemes_for_establishment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The schemes mentioned are the 'Sub-Mission on Polytechnics' and initiatives for educationally backward districts/left-wing extremism affected areas. The concerned State Government/UT must apply online on the AICTE Web Portal, and the application will go through scrutiny committees before approval.")
        return []