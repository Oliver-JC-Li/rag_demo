<!DOCTYPE html>
<!-- saved from url=(0078)https://github.com/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/light-74231a1f3bbb.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/dark-8a995f0bacd4.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-f37fb7684b1f.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-9ac301c3ebe5.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-cd826e8636dc.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-f91b0f603451.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-83beb16e0ecf.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-6e122dab64fc.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-18119e682df0.css">

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-primitives-225433424a87.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-cba26849680f.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/global-e516bfcd8d00.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/github-f98cfa35d7b2.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/repository-4fce88777fa8.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/code-0210be90f4d3.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["contentful_lp_flex_features_actions","contentful_lp_flex_features_codespaces","contentful_lp_flex_features_code_review","contentful_lp_flex_features_code_search","contentful_lp_flex_features_discussions","contentful_lp_flex_features_issues","copilot_new_immersive_references_ui","copilot_immersive_issue_preview","copilot_chat_interview_survey","copilot_chat_attach_images","copilot_chat_attachments","copilot_chat_custom_instructions","copilot_chat_repo_custom_instructions_preview","copilot_chat_show_model_picker_on_retry","copilot_chat_opening_thread_switch","copilot_chat_wholearea_dd","copilot_dotcom_chat_file_upload","copilot_no_floating_button","copilot_ui_refs","copilot_topics_as_references","copilot_read_shared_conversation","copilot_duplicate_thread","copilot_share_active_subthread","copilot_share_forbidden_error","copilot_free_to_paid_telem","dotcom_chat_client_side_skills","failbot_handle_non_errors","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","github_models_gateway","github_models_gateway_parse_params","github_models_o3_mini_streaming","insert_before_patch","issues_advanced_search","issues_advanced_search_has_filter","issues_react_remove_placeholders","issues_react_blur_item_picker_on_close","issues_advanced_search_nested_ownership_filters","issues_dashboard_no_redirects","marketing_pages_search_explore_provider","memex_roadmap_drag_style","primer_react_css_modules_ga","primer_react_select_panel_with_modern_action_list","remove_child_patch","repository_suggester_elastic_search","sample_network_conn_type","swp_enterprise_contact_form","site_copilot_pro_plus","site_proxima_australia_update","viewscreen_sandbox","issues_react_create_milestone","lifecycle_label_name_updates","item_picker_new_select_panel","copilot_task_oriented_assistive_prompts","issues_react_feature_preview_is_over","codespaces_prebuild_region_target_update","use_paginated_org_picker_cost_center_form","copilot_code_review_sign_up_closed","billing_usage_report_banner_notifications"],"login":"Oliver-JC-Li"}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/wp-runtime-9b76f6408d72.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover_js-9da652f58479.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_arianotify-polyfill_ariaNotify-polyfill_js-node_modules_github_mi-3abb8f-46b9f4874d95.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_failbot_failbot_ts-952d624642a1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/environment-f04cb2a9fc8c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_primer_behaviors_dist_esm_index_mjs-0dbb79f97f8f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-f690fd9ae3d5.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_relative-time-element_dist_index_js-62d275b7ddd9.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-8e9f78-a90ac05d2469.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_text-expander-element_dist_index_js-78748950cb0c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-b5f1d7-a1760ffda83d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_markdown-toolbar-element_dist_index_js-ceef33f593fa.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-c44a69-ad9a1d467623.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/github-elements-34dba4fe8c3b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/element-registry-e5a853ea2949.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-2906d7-2a07a295af40.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_lit-html_lit-html_js-be8cb88f481b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_morphdom_dist_morphdom-e-7c534c-a4a1922eb55f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-a03ee12d659a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-b6294cf703b7.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_color-convert_index_js-e3180fe3bcb3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-947061-e7a6c4a19f98.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_updatable-content_updatable-content_ts-62f3e9c52ece.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-900dde-768abe60b1f8.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/app_assets_modules_github_sticky-scroll-into-view_ts-3e000c5d31a9.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-d0d0a6-e7f74ee74d91.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-4bcbbbfbe1d4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/behaviors-ba450e1a8c71.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-f6223d90c7ba.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/notifications-global-01e85cd1be94.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-26cce2010167.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/code-menu-d6d3c94ee97e.js"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/primer-react-20836f3e2db3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/react-core-4e4deaa097d6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/react-lib-1622bd1e542f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/octicons-react-cf2f2ab8dab4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-41b1a8-6444bd9652c1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-e7dcdd-9a233856b02c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-55fea94174bf.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_dompurify_dist_purify_es_mjs-dd1d3ea6a436.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_lodash-es__Stack_js-node_modules_lodash-es__Uint8Array_js-node_modules_l-4faaa6-4a736fde5c2f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_lodash-es__baseIsEqual_js-8929eb9718d5.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_react-intersection-observer_dist_index_mjs-node_modules_react-virtual_di-0c3a9a-39ed17df71a8.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_focus-visible_dist_focus-visible_js-node_modules_fzy_js_index_js-node_mo-08d6cf-a84e5768db3f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_aria-live_aria-live_ts-ui_packages_history_history_ts-ui_packages_promise-with-re-01dc80-b13b6c1d97b0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_paths_index_ts-7488e96144d4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_ref-selector_RefSelector_tsx-7496afc3784d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-762eaa-bac5b6fc3f70.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_code-view-shared_utilities_web-worker_ts-ui_packages_code-view-shared_worker-jobs-7e435b-6499ef73cd7c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_app-uuid_app-uuid_ts-ui_packages_document-metadata_document-metadata_ts-ui_packag-4d8de9-fb57cda8a9d3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_code-view-shared_hooks_use-canonical-object_ts-ui_packages_code-view-shared_hooks-c2dbff-923a12b3d018.js"></script>

<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/react-code-view-742c70654730.js"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-react.0c87ead6152dce0ce7cf.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/react-code-view.91744b0963019bd58290.module.css">


  



  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  


      
      


      


      
      
      

        


  <meta http-equiv="x-pjax-version" content="e3280413fe0f1864ab68956ff4193e103d34488109d53e1866baf5b0bf35b6cb" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="e26f9f0ba624ee85cc7ac057d8faa8618a4f25a85eab052c33d018ac0f6b1a46" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="0d2053b2848bff67d4b37640c4c5d28a5ae47fe01d85cb73847ae75d9297a807" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="e4c355a7631fb685e89523e7628cb9d12b3b48840b626a62468ad496d0d4aa48" data-turbo-track="reload">

  

      

    
  

  



    

    


  

  

  

  
  
  





  

  <style data-styled="active" data-styled-version="5.3.11"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/notifications-subscriptions-menu.1bcff9205c241e99cff2.module.css"><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-94dc7a2157c1.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-70450e-4b93df70b903.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/app_assets_modules_github_ref-selector_ts-52913063a0b9.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/codespaces-b419a25ee02f.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-3eebbd-0763620ad7bf.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_delegated-events_di-e161aa-9d41fb1b6c9e.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_remote--3c9c82-b71ef90fbdc7.js"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/repositories-26e6935ed39d.js"></script><style type="text/css" id="ms-consent-banner-theme-styles"></style><script type="application/json" id="client-env">{"locale":"en","featureFlags":["contentful_lp_flex_features_actions","contentful_lp_flex_features_codespaces","contentful_lp_flex_features_code_review","contentful_lp_flex_features_code_search","contentful_lp_flex_features_discussions","contentful_lp_flex_features_issues","copilot_new_immersive_references_ui","copilot_immersive_issue_preview","copilot_chat_interview_survey","copilot_chat_attach_images","copilot_chat_attachments","copilot_chat_custom_instructions","copilot_chat_repo_custom_instructions_preview","copilot_chat_show_model_picker_on_retry","copilot_chat_opening_thread_switch","copilot_chat_wholearea_dd","copilot_dotcom_chat_file_upload","copilot_no_floating_button","copilot_ui_refs","copilot_topics_as_references","copilot_read_shared_conversation","copilot_duplicate_thread","copilot_share_active_subthread","copilot_share_forbidden_error","copilot_free_to_paid_telem","dotcom_chat_client_side_skills","failbot_handle_non_errors","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","github_models_gateway","github_models_gateway_parse_params","github_models_o3_mini_streaming","insert_before_patch","issues_advanced_search","issues_advanced_search_has_filter","issues_react_remove_placeholders","issues_react_blur_item_picker_on_close","issues_advanced_search_nested_ownership_filters","issues_dashboard_no_redirects","marketing_pages_search_explore_provider","memex_roadmap_drag_style","primer_react_css_modules_ga","primer_react_select_panel_with_modern_action_list","remove_child_patch","report_hydro_web_vitals","repository_suggester_elastic_search","sample_network_conn_type","swp_enterprise_contact_form","site_copilot_pro_plus","site_proxima_australia_update","viewscreen_sandbox","issues_react_create_milestone","lifecycle_label_name_updates","item_picker_new_select_panel","copilot_task_oriented_assistive_prompts","issues_react_feature_preview_is_over","codespaces_prebuild_region_target_update","use_paginated_org_picker_cost_center_form","copilot_code_review_sign_up_closed","billing_usage_report_banner_notifications"],"login":"Oliver-JC-Li"}</script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/app_assets_modules_github_blob-anchor_ts-ui_packages_code-nav_code-nav_ts-ui_packages_filter--8253c1-91468a3354f9.js"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>rag_demo/stop360_multiturn_rag_v2.py at main · Oliver-JC-Li/rag_demo</title><meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient=""><meta name="route-controller" content="blob" data-turbo-transient=""><meta name="route-action" content="show" data-turbo-transient=""><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="CF40:03A1:7C4BE46:ACA4F45:67FD9994" data-turbo-transient="true"><meta name="html-safe-nonce" content="c2e28b88812841f5d7ecce61fe4aedef88ff090d71bed3c51f346f5e35000102" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9PbGl2ZXItSkMtTGkvcmFnX2RlbW8vYmxvYi9tYWluL3N0b3AzNjBfbXVsdGl0dXJuX3JhZ192Mi5weSIsInJlcXVlc3RfaWQiOiJDRjQwOjAzQTE6N0M0QkU0NjpBQ0E0RjQ1OjY3RkQ5OTk0IiwidmlzaXRvcl9pZCI6IjQ3MDE0NDQwNDIwMTAwMzM5MjIiLCJyZWdpb25fZWRnZSI6ImlhZCIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-turbo-transient="true"><meta name="visitor-hmac" content="90b1dfbee161f4222343929c427b9b377f209b423f7466fc5b7ba37df7b01d5d" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:861863149" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_source" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="72470431"><meta name="octolytics-actor-login" content="Oliver-JC-Li"><meta name="octolytics-actor-hash" content="fc3c9ec90a4f5cd37ba5e598708ed278723d3b2f5e73e4a3e761d9ccb6625ac6"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true"><meta name="user-login" content="Oliver-JC-Li"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""><meta data-hydrostats="publish"><meta name="go-import" content="github.com/Oliver-JC-Li/rag_demo git https://github.com/Oliver-JC-Li/rag_demo.git"><meta name="octolytics-dimension-user_id" content="72470431"><meta name="octolytics-dimension-user_login" content="Oliver-JC-Li"><meta name="octolytics-dimension-repository_id" content="861863149"><meta name="octolytics-dimension-repository_nwo" content="Oliver-JC-Li/rag_demo"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="861863149"><meta name="octolytics-dimension-repository_network_root_nwo" content="Oliver-JC-Li/rag_demo"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><meta name="release" content="255ac5a68403ac68e9140ffcfa687fa70b1c189b"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg" data-base-href="https://github.githubassets.com/favicons/favicon"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-in env-production page-responsive" style="overflow-wrap: break-word; --dialog-scrollgutter: 12px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_ui-commands_ui-commands_ts-2d52c8e72e64.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/keyboard-shortcuts-dialog-2560f573c7ca.js"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-react.0c87ead6152dce0ce7cf.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:r3c:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>




      

          

              <header class="AppHeader" role="banner">
  <h2 class="sr-only">Navigation Menu</h2>

    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-9b940ab7-fabb-4769-9c82-637e6e325987" id="dialog-show-dialog-9b940ab7-fabb-4769-9c82-637e6e325987" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button p-0 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-9b940ab7-fabb-4769-9c82-637e6e325987" aria-modal="true" aria-labelledby="dialog-9b940ab7-fabb-4769-9c82-637e6e325987-title" aria-describedby="dialog-9b940ab7-fabb-4769-9c82-637e6e325987-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-left SidePanel Overlay--disableScroll">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-9b940ab7-fabb-4769-9c82-637e6e325987-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.9225 1 1 5.9225 1 12C1 16.8675 4.14875 20.9787 8.52125 22.4362C9.07125 22.5325 9.2775 22.2025 9.2775 21.9137C9.2775 21.6525 9.26375 20.7862 9.26375 19.865C6.5 20.3737 5.785 19.1912 5.565 18.5725C5.44125 18.2562 4.905 17.28 4.4375 17.0187C4.0525 16.8125 3.5025 16.3037 4.42375 16.29C5.29 16.2762 5.90875 17.0875 6.115 17.4175C7.105 19.0812 8.68625 18.6137 9.31875 18.325C9.415 17.61 9.70375 17.1287 10.02 16.8537C7.5725 16.5787 5.015 15.63 5.015 11.4225C5.015 10.2262 5.44125 9.23625 6.1425 8.46625C6.0325 8.19125 5.6475 7.06375 6.2525 5.55125C6.2525 5.55125 7.17375 5.2625 9.2775 6.67875C10.1575 6.43125 11.0925 6.3075 12.0275 6.3075C12.9625 6.3075 13.8975 6.43125 14.7775 6.67875C16.8813 5.24875 17.8025 5.55125 17.8025 5.55125C18.4075 7.06375 18.0225 8.19125 17.9125 8.46625C18.6138 9.23625 19.04 10.2125 19.04 11.4225C19.04 15.6437 16.4688 16.5787 14.0213 16.8537C14.42 17.1975 14.7638 17.8575 14.7638 18.8887C14.7638 20.36 14.75 21.5425 14.75 21.9137C14.75 22.2025 14.9563 22.5462 15.5063 22.4362C19.8513 20.9787 23 16.8537 23 12C23 5.9225 18.0775 1 12 1Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-9b940ab7-fabb-4769-9c82-637e6e325987" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="dialog-9b940ab7-fabb-4769-9c82-637e6e325987-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-target="nav-list.topLevelList" data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-936f6493-fc99-4a1c-b3f0-ce9bb348c6eb" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-9d8ed2c7-a2d9-4c41-bde7-651c10915eef" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-5eb9ae21-2684-4ee3-9383-baa2582f2ab6" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROJECTS&quot;,&quot;label&quot;:null}" id="item-81175607-e334-44fd-93b8-cc71afb0458e" href="https://github.com/projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-e35b6bcf-e171-4fb8-a143-19bfd101f61a" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-6818cdce-c92e-4ef9-9907-b306761b28db" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;COPILOT&quot;,&quot;label&quot;:null}" id="item-56bef447-b6cc-4559-9ade-4c11ccf2d290" href="https://github.com/copilot" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Copilot
</span>      
</a>
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-ea799a09-b50c-486f-be84-def6e8a24467" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-e12cedd0-8d65-4b10-9f9f-95d9fe6d5357" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span>      
</a>
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <span data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">© 2025 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex flex-wrap text-small text-light">
          <a target="_blank" href="https://github.com/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog/" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="https://github.com/security" data-view-component="true" class="Link mr-2">Security</a>
          <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>

</div></div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>

  </include-fragment>
</deferred-side-panel>

        <a class="AppHeader-logo ml-1 " href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
          <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path d="M12 1C5.9225 1 1 5.9225 1 12C1 16.8675 4.14875 20.9787 8.52125 22.4362C9.07125 22.5325 9.2775 22.2025 9.2775 21.9137C9.2775 21.6525 9.26375 20.7862 9.26375 19.865C6.5 20.3737 5.785 19.1912 5.565 18.5725C5.44125 18.2562 4.905 17.28 4.4375 17.0187C4.0525 16.8125 3.5025 16.3037 4.42375 16.29C5.29 16.2762 5.90875 17.0875 6.115 17.4175C7.105 19.0812 8.68625 18.6137 9.31875 18.325C9.415 17.61 9.70375 17.1287 10.02 16.8537C7.5725 16.5787 5.015 15.63 5.015 11.4225C5.015 10.2262 5.44125 9.23625 6.1425 8.46625C6.0325 8.19125 5.6475 7.06375 6.2525 5.55125C6.2525 5.55125 7.17375 5.2625 9.2775 6.67875C10.1575 6.43125 11.0925 6.3075 12.0275 6.3075C12.9625 6.3075 13.8975 6.43125 14.7775 6.67875C16.8813 5.24875 17.8025 5.55125 17.8025 5.55125C18.4075 7.06375 18.0225 8.19125 17.9125 8.46625C18.6138 9.23625 19.04 10.2125 19.04 11.4225C19.04 15.6437 16.4688 16.5787 14.0213 16.8537C14.42 17.1975 14.7638 17.8575 14.7638 18.8887C14.7638 20.36 14.75 21.5425 14.75 21.9137C14.75 22.2025 14.9563 22.5462 15.5063 22.4362C19.8513 20.9787 23 16.8537 23 12C23 5.9225 18.0775 1 12 1Z"></path>
</svg>
        </a>

            <div class="AppHeader-context">
  <div class="AppHeader-context-compact">
      <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: Oliver-JC-Li / rag_demo" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">  <span class="Button-content">
    <span class="Button-label"><span class="AppHeader-context-compact-lead">
              <span class="AppHeader-context-compact-parentItem">Oliver-JC-Li</span>

            <span class="no-wrap">&nbsp;/</span>

        </span>

        <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate">
  

  <span class="Truncate-text ">rag_demo</span>

</strong></span>
  </span>
</button>

<dialog-helper>
  <dialog id="context-region-dialog" aria-modal="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="context-region-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">      <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Oliver-JC-Li&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/Oliver-JC-Li" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
              <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-person mr-1">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>

            Oliver-JC-Li
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;rag_demo&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/Oliver-JC-Li/rag_demo" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
              <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

            rag_demo
        </span>

</a>
    </li>
</ul>

</div>
      </scrollable-region>
      
</dialog></dialog-helper>

  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Oliver-JC-Li&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/Oliver-JC-Li/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Oliver-JC-Li" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

            Oliver-JC-Li
        </span>

</a>
        <span class="AppHeader-context-item-separator">
          <span class="sr-only">/</span>
          <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
          </svg>
        </span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;rag_demo&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/Oliver-JC-Li/rag_demo" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

            rag_demo
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search">
              


<qbsearch-input class="search-input" data-scope="repo:Oliver-JC-Li/rag_demo" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="BahzWpIdO1JAW9lKGZHuhGaO4Ng_VkS1i_qYrZlZl5_lsGAHfTkg4Y4aAvLwjEY9LcaaI3L4qdgDt-yeBK3T4g" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="Oliver-JC-Li/rag_demo" data-current-org="" data-current-owner="Oliver-JC-Li" data-logged-in="true" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control AppHeader-search-control-overflow">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}" aria-describedby="search-error-message-flash">
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-249d9048-590e-4525-8921-021a4020ed66" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-249d9048-590e-4525-8921-021a4020ed66" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="8SBx5RKW8YsPhXJu3dk2RQicAbV8aiF05ER-pUkOYCoRech0DNpmmM3htrjJ4-9GG2UkYykcj8BIn_8GCbk5Nw">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="wvz6IpvvFUwepXoKgfDTfoQMPrf-GccRJyhs4-DM5b4jp7tFY80VORjoivuN4wyNKLMhk4sMiW52UbVdzWfsAA">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="" only-validate-on-blur="true">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="twKwo5YKTOL3LO1pM9swXAMB-RNgManlaU5mFUAJer5QkcwjDXLnrw-JNXCQhNaGJF_uQlVH2Ntj86-pzNTmiA" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="s-ZlK-G-CeShN7JQSz2IRvcoWbMZCqQAvRXyPRET2ftwDR-HTnnw_hRKvpG0ylaULoTZYWp9_Y3neVHx6VWZ7A" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">


          </div>

        
          <div class="AppHeader-CopilotChat hide-sm hide-md">
  <react-partial-anchor data-catalyst="">
      <a href="https://github.com/copilot" data-target="react-partial-anchor.anchor" id="copilot-chat-header-button" aria-expanded="false" aria-controls="copilot-chat-panel" aria-labelledby="tooltip-95487f54-5122-4ebd-8ba7-ed9abbdfda23" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonLeft">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot Button-visual">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-95487f54-5122-4ebd-8ba7-ed9abbdfda23" for="copilot-chat-header-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Chat with Copilot</tool-tip>

    
  
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-9743ca933872.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_react-relay_index_js-137de9a77ac9.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_remark-gfm_lib_index_js-node_modules_remark-parse_lib_index_js-node_modu-44d0fc-3771aaaad894.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_highlight_js_es_core_js-node_modules_lowlight_lib_all_js-be89bc04c72d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_hastscript_lib_index_js-node_modules_react-markdown_lib_index_js-node_mo-68849e-87072326f2b3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_accname_dist_access-a7695e-94bc658fafd2.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_combobox-nav_dist_index_js-node_modules_github_hotkey_dist_index_-9adaba-5a418e410b38.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_relay-environment_relay-environment_ts-ui_packages_item-picker_components_Reposit-97e2e1-5e6ddc7e0793.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_utils_copilot-chat-helpers_ts-3453c8fa733b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-markdown_MarkdownRenderer_tsx-6132f81f9b6e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_utils_CopilotChatContext_tsx-3d67cfeec248.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_components_ChatInput_tsx-ui_packages_copilot-chat_components_LegalDi-36d9b7-21ad8d6199ad.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_hooks_use-chat-message-behavior_ts-ui_packages_copilot-chat_hooks_us-f9f91d-1b0b49c73228.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_components_Chat_tsx-ui_packages_icon-button-with-tooltip_IconButtonW-1ba5d9-1ca50e989548.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/copilot-chat-5a2d01360b0a.js"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-react.0c87ead6152dce0ce7cf.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/ui_packages_copilot-chat_hooks_use-chat-message-behavior_ts-ui_packages_copilot-chat_hooks_us-f9f91d.93c211483b1dd073eb6b.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/copilot-chat.171ab343c672187140e7.module.css">
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/copilot-markdown-rendering-f6845e8f5d6b.css">
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/primer-react-20836f3e2db3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/react-core-4e4deaa097d6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/react-lib-1622bd1e542f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/octicons-react-cf2f2ab8dab4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-41b1a8-6444bd9652c1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-e7dcdd-9a233856b02c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-55fea94174bf.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_dompurify_dist_purify_es_mjs-dd1d3ea6a436.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-9743ca933872.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_react-relay_index_js-137de9a77ac9.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_remark-gfm_lib_index_js-node_modules_remark-parse_lib_index_js-node_modu-44d0fc-3771aaaad894.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_highlight_js_es_core_js-node_modules_lowlight_lib_all_js-be89bc04c72d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_hastscript_lib_index_js-node_modules_react-markdown_lib_index_js-node_mo-68849e-87072326f2b3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_accname_dist_access-a7695e-94bc658fafd2.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_focus-visible_dist_focus-visible_js-node_modules_fzy_js_index_js-node_mo-08d6cf-a84e5768db3f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/vendors-node_modules_github_combobox-nav_dist_index_js-node_modules_github_hotkey_dist_index_-9adaba-5a418e410b38.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_paths_index_ts-7488e96144d4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_ui-commands_ui-commands_ts-2d52c8e72e64.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_relay-environment_relay-environment_ts-ui_packages_item-picker_components_Reposit-97e2e1-5e6ddc7e0793.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_utils_copilot-chat-helpers_ts-3453c8fa733b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-markdown_MarkdownRenderer_tsx-6132f81f9b6e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_utils_CopilotChatContext_tsx-3d67cfeec248.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_components_ChatInput_tsx-ui_packages_copilot-chat_components_LegalDi-36d9b7-21ad8d6199ad.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_hooks_use-chat-message-behavior_ts-ui_packages_copilot-chat_hooks_us-f9f91d-1b0b49c73228.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_copilot-chat_components_Chat_tsx-ui_packages_icon-button-with-tooltip_IconButtonW-1ba5d9-1ca50e989548.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/copilot-chat-5a2d01360b0a.js"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-react.0c87ead6152dce0ce7cf.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/ui_packages_copilot-chat_hooks_use-chat-message-behavior_ts-ui_packages_copilot-chat_hooks_us-f9f91d.93c211483b1dd073eb6b.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/copilot-chat.171ab343c672187140e7.module.css">

<react-partial partial-name="copilot-chat" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"currentTopic":{"id":861863149,"name":"rag_demo","ownerLogin":"Oliver-JC-Li","ownerType":"User","readmePath":"README.md","description":"This is a repository to demonstrate research study QA chatbot with RAG","commitOID":"a2d9f6b8efc77b42fc6dab664f8ab4b036c0ac8f","ref":"refs/heads/main","refInfo":{"name":"main","type":"branch"},"visibility":"public","languages":[{"name":"Python","percent":100.0}],"customInstructions":[]},"findFileWorkerPath":"/assets-cdn/worker/find-file-worker-7d7eb7c71814.js","renderPopover":false,"renderBetaLabel":false,"chatIsVisible":true,"chatVisibleSettingPath":"/users/Oliver-JC-Li/copilot_chat/settings/copilot_chat_visibility","ssoOrganizations":[],"agentsPath":"/github-copilot/chat/agents","apiURL":"https://api.individual.githubcopilot.com","currentUserLogin":"Oliver-JC-Li","customInstructions":null,"renderKnowledgeBases":false,"optedInToPreviewFeatures":false,"optedInToUserFeedback":false,"renderAttachKnowledgeBaseHerePopover":true,"renderKnowledgeBaseAttachedToChatPopover":true,"personalInstructions":null,"reviewLab":false,"realIp":null,"scrollToTop":false,"hasCEorCBAccess":false,"licenseType":"unlicensed","quotas":null,"icebreakers":[{"type":"functional","data":[{"id":"open-issues-in-react","message":"Get a list of the latest open issues in the facebook/react repository, including all their labels.","titleHtml":"Open issues in \u003cspan class=\"fgColor-muted\"\u003efacebook/react\u003c/span\u003e","icon":"issue-opened","color":"var(--display-green-fgColor)"},{"id":"pulls-in-vscode","message":"Retrieve pull requests in microsoft/vscode.","titleHtml":"Pull requests in \u003cspan class=\"fgColor-muted\"\u003emicrosoft/vscode\u003c/span\u003e","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"commits-in-linux","message":"Show recent commits in torvalds/linux.","titleHtml":"Recent commits in \u003cspan class=\"fgColor-muted\"\u003etorvalds/linux\u003c/span\u003e","icon":"git-commit","color":"var(--display-blue-fgColor)"},{"id":"my-latest-issues","message":"Find the five latest issues assigned to me.","titleHtml":"Find issues assigned to me","icon":"issue-opened","color":"var(--display-green-fgColor)"},{"id":"latest-node-release","message":"Fetch the latest release of nodejs/node and highlight the changes.","titleHtml":"Latest \u003cspan class=\"fgColor-muted\"\u003enodejs/node\u003c/span\u003e release","icon":"tag","color":"var(--display-purple-fgColor)"},{"id":"create-profile-readme","message":"Create a profile README for $$USERNAME$$.","titleHtml":"Create a profile README for me","icon":"rocket","color":"var(--display-pink-fgColor)"},{"id":"bugs-in-primer","message":"Show recent bugs in primer/react.","titleHtml":"Recent bugs in \u003cspan class=\"fgColor-muted\"\u003eprimer/react\u003c/span\u003e","icon":"bug","color":"var(--display-purple-fgColor)"},{"id":"my-open-pulls","message":"Find my open pull requests.","titleHtml":"My open pull requests","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"generate-html-calculator","message":"Generate a simple calculator using HTML, CSS, and JavaScript.","titleHtml":"Generate an HTML/JS calculator","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"python-strong-password-endpoint","message":"Generate a Python endpoint for signing up that only allows strong passwords.","titleHtml":"Python password endpoint","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"rails-auth-endpoint","message":"Generate a Rails endpoint for authenticating with email and password.","titleHtml":"Rails authentication endpoint","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"python-pandas-data-analysis","message":"Write a Python script that analyzes a dataset using Pandas.","titleHtml":"Python Panda data analysis","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explain-restful-basics","message":"Explain REST architectural principles and how to implement RESTful web services.","titleHtml":"Explain RESTful basics","icon":"book","color":"var(--display-blue-fgColor)"},{"id":"compare-http-post-vs-put","message":"Compare HTTP POST and PUT methods, explaining their proper usage in RESTful APIs.","titleHtml":"Compare HTTP POST vs PUT","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explain-json-content-types","message":"Explain proper JSON MIME types and content-type headers for different scenarios and platforms.","titleHtml":"Explain JSON content types","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"compare-dates-and-times","message":"Explain strategies for accurately comparing dates and times across different timezones and formats.","titleHtml":"Compare dates and times","icon":"clock","color":"var(--display-blue-fgColor)"},{"id":"compare-json-comment-options","message":"Explain JSON syntax limitations regarding comments and alternative approaches for documentation.","titleHtml":"Compare JSON comment options","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explain-stack-and-heap-memory","message":"Compare stack and heap memory allocation, their characteristics, and use cases in programming.","titleHtml":"Explain stack and heap memory","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"compare-api-version-strategies","message":"Explain different approaches to API versioning including URL, header, and content negotiation.","titleHtml":"Compare API version strategies","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"how-to-fix-git-submodules","message":"Troubleshoot and resolve issues with uninitialized Git submodules, explaining initialization commands and common pitfalls.","titleHtml":"How to fix Git submodules","icon":"git-merge","color":"var(--display-green-fgColor)"},{"id":"compare-git-fork-and-clone","message":"Compare and contrast Git clones versus forks, explaining their technical differences, use cases, and relationship to original repositories.","titleHtml":"Compare Git fork and clone","icon":"git-branch","color":"var(--display-green-fgColor)"},{"id":"explain-pull-request-basics","message":"Walk through the complete process of creating, submitting, and managing pull requests on GitHub, from forking to merging.","titleHtml":"Explain pull request basics","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"git-history-cleanup-guide","message":"Provide a complete guide to permanently removing files from Git history, including BFG and filter-repo approaches with safety considerations.","titleHtml":"Git history cleanup guide","icon":"trash","color":"var(--display-blue-fgColor)"},{"id":"git-credential-management","message":"Explain the different methods for caching HTTPS credentials when pushing Git commits, including credential helpers, personal access tokens, and their security implications.","titleHtml":"Git credential management","icon":"key","color":"var(--display-purple-fgColor)"},{"id":"compare-origin-and-upstream","message":"Explain the conceptual and functional differences between origin and upstream remote repositories in Git, with examples of how they're used in workflow.","titleHtml":"Compare origin and upstream","icon":"git-branch","color":"var(--display-green-fgColor)"},{"id":"how-to-download-github-folders","message":"Describe various methods to download specific folders from GitHub repositories without cloning the entire project.","titleHtml":"How to download GitHub folders","icon":"download","color":"var(--display-blue-fgColor)"},{"id":"git-path-configurations","message":"Provide cross-platform instructions for properly configuring GitHub Desktop to include Git in the system PATH, enabling command-line Git operations alongside the GUI client on Windows, macOS, and Linux systems.","titleHtml":"Git PATH configurations","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explain-fork-sync-process","message":"Provide step-by-step instructions for synchronizing a forked GitHub repository with its original upstream repository, including both command line methods and GitHub interface options.","titleHtml":"Explain fork sync process","icon":"git-merge","color":"var(--display-green-fgColor)"},{"id":"list-git-history-danger-zones","message":"List and explain potentially dangerous Git commands that can alter repository history, with guidelines on when and how to use them safely.","titleHtml":"List Git history danger zones","icon":"history","color":"var(--display-blue-fgColor)"},{"id":"explain-cli-repository-setup","message":"Explain methods for creating GitHub repositories entirely from the command line using GitHub CLI, API tokens, and other headless approaches.","titleHtml":"Explain CLI repository setup","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"how-to-migrate-git-remote","message":"Detail the process of migrating an existing Git repository to a different remote server while preserving history, branches, and tags, with command examples.","titleHtml":"How to migrate Git remote","icon":"git-commit","color":"var(--display-blue-fgColor)"},{"id":"compare-git-and-github","message":"Explain the fundamental differences between Git (the distributed version control system) and GitHub (the web-based hosting service), clarifying their relationship, unique features, and how they complement each other in modern development workflows.","titleHtml":"Compare Git and GitHub","icon":"git-branch","color":"var(--display-green-fgColor)"},{"id":"learn-git-multi-remote-setup","message":"Explain the process of configuring a Git repository to push commits simultaneously to multiple remote repositories, including setting up multiple remotes and creating automated push workflows.","titleHtml":"Learn Git multi remote setup","icon":"git-commit","color":"var(--display-blue-fgColor)"},{"id":"convert-single-branch-clone","message":"Explain methods for converting a single-branch Git clone into a full repository clone with access to all remote branches, including fetch commands and configuration changes.","titleHtml":"Convert single branch clone","icon":"git-branch","color":"var(--display-green-fgColor)"},{"id":"multiple-github-account-guide","message":"Provide step-by-step instructions for configuring and managing multiple GitHub accounts on a single computer, including SSH key setup and Git configuration.","titleHtml":"Multiple GitHub account guide","icon":"mark-github","color":"var(--display-purple-fgColor)"},{"id":"explore-java-map-iterations","message":"Compare different methods for efficiently iterating over Map entries in Java.","titleHtml":"Explore Java Map Iterations","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"understand-java-access-levels","message":"Explain differences between Java's access modifiers with practical examples.","titleHtml":"Understand Java access levels","icon":"lock","color":"var(--display-purple-fgColor)"},{"id":"compare-java-password-types","message":"Compare char[] vs String for password storage in Java with security implications.","titleHtml":"Compare Java password types","icon":"key","color":"var(--display-purple-fgColor)"},{"id":"compare-java-hashmap-hashtable","message":"Compare HashMap and Hashtable in Java, explaining their key differences including thread safety, null handling, synchronization overhead, and performance characteristics with practical examples.","titleHtml":"Compare Java HashMap/Hashtable","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-java-array-sorting-perf","message":"Explain how CPU branch prediction and cache optimization affect Java array processing performance, demonstrating the speed difference between sorted and unsorted arrays with examples.","titleHtml":"Learn Java array sorting perf","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"java-operator-casting-basics","message":"Explain why compound assignment operators in Java don't require explicit casting.","titleHtml":"Java operator casting basics","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explain-java-char-for-password","message":"Explain why char[] is preferred over String for passwords in Java, including security implications.","titleHtml":"Explain Java char[] for password","icon":"key","color":"var(--display-purple-fgColor)"},{"id":"compare-java-pass-by-value-ref","message":"Explain whether Java is pass-by-reference or pass-by-value with examples.","titleHtml":"Compare Java pass by value/ref","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-js-import-patterns","message":"Explain different approaches to importing JavaScript files, including modern ES6 modules.","titleHtml":"Learn JS import patterns","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explore-js-array-loops","message":"Compare different methods for iterating over arrays in JavaScript with use cases.","titleHtml":"Explore JS array loops","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"understand-js-strict-mode-usage","message":"Explain the purpose and benefits of strict mode in JavaScript, including common pitfalls it prevents.","titleHtml":"Understand JS strict mode usage","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-js-closures","message":"Explain JavaScript closure concept with practical examples showing scope and data privacy.","titleHtml":"Learn JS closures","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"compare-js-equality-operators","message":"Compare the behavior and use cases of == and === operators in JavaScript, explaining type coercion and best practices.","titleHtml":"Compare JS equality operators","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-js-sleep-function","message":"Explain how to implement delay/sleep functionality in JavaScript using promises and async/await.","titleHtml":"Learn JS sleep function","icon":"clock","color":"var(--display-blue-fgColor)"},{"id":"compare-js-substring-checks","message":"Compare methods for checking substrings in JavaScript strings, with performance considerations.","titleHtml":"Compare JS substring checks","icon":"search","color":"var(--display-blue-fgColor)"},{"id":"how-to-handle-js-async-response","message":"Explain handling asynchronous operations in JavaScript using promises, async/await, and callbacks.","titleHtml":"How to handle JS async response","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"python-slice-syntax","message":"Explain Python's list slicing syntax, including step values and negative indices.","titleHtml":"Python slice syntax","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"how-to-flatten-lists-in-python","message":"Compare methods for flattening nested lists in Python, from simple to complex cases.","titleHtml":"How to flatten lists in Python","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-python-main-check","message":"Explain the purpose and usage of if name == \"main\" in Python, including module behavior and best practices.","titleHtml":"Learn Python main check","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"python-env-variables-guide","message":"Explain how to access and manage environment variables in Python applications.","titleHtml":"Python env variables guide","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-python-star-operators","message":"Explain the difference between single and double asterisk operators in Python for parameter packing and unpacking.","titleHtml":"Learn Python star operators","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explain-python-yield","message":"Explain Python generators and the yield keyword with examples of memory-efficient iteration.","titleHtml":"Explain Python yield","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"python-variable-passing-guide","message":"Explain Python's pass-by-object-reference behavior with examples of mutable and immutable objects.","titleHtml":"Python variable passing guide","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"generate-curl-json-post","message":"Demonstrate how to send JSON data using cURL, including headers and authentication.","titleHtml":"Generate cURL JSON POST","icon":"terminal","color":"var(--display-gray-fgColor)"},{"id":"show-linux-text-search","message":"Demonstrate commands and techniques for searching text within files on Linux systems.","titleHtml":"Show Linux text search","icon":"search","color":"var(--display-blue-fgColor)"},{"id":"learn-to-check-visibility-in-js","message":"Demonstrate methods for detecting hidden elements in JavaScript, including various visibility states.","titleHtml":"Learn to check visibility in JS","icon":"eye","color":"var(--display-purple-fgColor)"},{"id":"find-bash-script-location","message":"Show methods for determining a Bash script's directory location during execution.","titleHtml":"Find Bash script location","icon":"terminal","color":"var(--display-gray-fgColor)"},{"id":"explain-special-char-escape","message":"Demonstrate different methods for escaping special characters in various programming contexts.","titleHtml":"Explain special char escape","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"show-directory-exists","message":"Show different methods for checking directory existence in Bash with error handling.","titleHtml":"Show directory exists","icon":"terminal","color":"var(--display-gray-fgColor)"},{"id":"webpage-redirect-methods","message":"Show different techniques for implementing webpage redirects using HTML, JavaScript and server-side approaches.","titleHtml":"Webpage redirect methods","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"branch-sync-patterns","message":"Demonstrate Git commands for synchronizing branches, including reset, rebase, and merge techniques with their implications.","titleHtml":"Branch sync patterns","icon":"git-merge","color":"var(--display-green-fgColor)"},{"id":"how-to-recover-deleted-git-files","message":"Demonstrate techniques for locating and recovering files that were deleted in previous commits, including Git log commands, filtering options, and restoration methods.","titleHtml":"How to recover deleted Git files","icon":"history","color":"var(--display-blue-fgColor)"},{"id":"how-to-load-remote-js-script","message":"Provide code examples and best practices for linking to and executing JavaScript files hosted on GitHub in web applications.","titleHtml":"How to load remote JS script","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"how-to-npm-install-from-github","message":"Demonstrate different methods for installing npm packages directly from GitHub repositories, including syntax examples and troubleshooting tips.","titleHtml":"How to npm install from GitHub","icon":"package","color":"var(--display-blue-fgColor)"},{"id":"demo-java-linkedlist-arraylist","message":"Show different methods for initializing ArrayLists in Java in a single line.","titleHtml":"Demo Java LinkedList/ArrayList","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-java-memory-issues","message":"Demonstrate common causes of memory leaks in Java and how to prevent them.","titleHtml":"Learn Java memory issues","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-java-stream-conversion","message":"Show different methods for converting an InputStream to a String in Java, comparing performance.","titleHtml":"Learn Java stream conversion","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"java-null-handling-patterns","message":"Demonstrate best practices for handling null values in Java using Optional and other patterns.","titleHtml":"Java null handling patterns","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"java-list-conversion-guide","message":"Show different approaches to convert arrays to ArrayLists in Java with examples.","titleHtml":"Java List conversion guide","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"js-email-validation-guide","message":"Demonstrate robust email validation techniques in JavaScript, from regex patterns to validation APIs.","titleHtml":"JS email validation guide","icon":"mail","color":"var(--display-blue-fgColor)"},{"id":"prototype-js-array-iteration","message":"Demonstrate methods for removing specific items from JavaScript arrays with examples.","titleHtml":"Prototype JS array iteration","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explore-js-object-checks","message":"Show different methods for detecting empty objects in JavaScript, considering various edge cases.","titleHtml":"Explore JS object checks","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"how-to-js-remove-object-props","message":"Demonstrate different methods for removing properties from JavaScript objects and their implications.","titleHtml":"How to JS remove object props","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"how-to-merge-python-dicts","message":"Show different methods for merging Python dictionaries, including dictionary unpacking and update methods.","titleHtml":"How to merge Python dicts","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"explore-python-ternary-syntax","message":"Demonstrate Python's ternary conditional operator with examples comparing it to traditional if-else statements.","titleHtml":"Explore Python ternary syntax","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"demo-python-loop-with-index","message":"Demonstrate different ways to access index values in Python for loops using enumerate and range.","titleHtml":"Demo Python loop with index","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"demo-sorting-python-dictionary","message":"Demonstrate methods for sorting Python dictionaries by values using different approaches and sorting criteria.","titleHtml":"Demo sorting Python dictionary","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"learn-python-file-checks","message":"Show methods for checking file existence in Python without raising exceptions.","titleHtml":"Learn Python file checks","icon":"file","color":"var(--display-blue-fgColor)"},{"id":"demo-python-run-system-command","message":"Demonstrate various methods for executing system commands in Python using subprocess and other modules.","titleHtml":"Demo Python run system command","icon":"terminal","color":"var(--display-gray-fgColor)"},{"id":"compare-python-method-decorators","message":"Compare @staticmethod and @classmethod decorators in Python, explaining their use cases.","titleHtml":"Compare Python method decorators","icon":"code","color":"var(--display-gray-fgColor)"}]},{"type":"instructional","data":[{"id":"what-can-i-do-with-github-copilot-chat","message":"What can I do with GitHub Copilot Chat?","titleHtml":"What can I do here?","icon":"light-bulb","color":"var(--display-purple-fgColor)"}]},{"type":"interactional","data":[{"id":"to-do-app-local-storage","message":"Create a to-do list application with local storage functionality.","titleHtml":"To-do list with local storage","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"digital-clock-time-zones","message":"Create a digital clock that displays the current time in different time zones.","titleHtml":"A digital time zone clock","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"weather-dashboard-app","message":"Develop a weather dashboard that fetches data from a public weather API.","titleHtml":"Develop a weather dashboard","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"create-joke-generator","message":"Create a random joke generator using an external API.","titleHtml":"Create a joke generator","icon":"code","color":"var(--display-gray-fgColor)"}]}],"canShareThread":true}}</script>
  <div data-target="react-partial.reactRoot"><div class="Box-sc-g0xbh4-0 bpDFns"></div><div class="Box-sc-g0xbh4-0 hmHhrt"></div><script type="application/json" id="__PRIMER_DATA_:r59:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>


    </react-partial-anchor>
  <react-partial-anchor data-catalyst="">
    <button id="global-copilot-menu-button" data-target="react-partial-anchor.anchor" aria-expanded="false" aria-labelledby="tooltip-ecdce549-65bf-4888-bd1a-3cc2c19d0a12" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonRight" aria-haspopup="true">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-ecdce549-65bf-4888-bd1a-3cc2c19d0a12" for="global-copilot-menu-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Open Copilot…</tool-tip>

    
  
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/global-copilot-menu-5fc34e842f83.js"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-react.0c87ead6152dce0ce7cf.module.css">

<react-partial partial-name="global-copilot-menu" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:r50:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>

    </react-partial-anchor>
</div>


        <div class="AppHeader-actions position-relative">
             <react-partial-anchor data-catalyst="">
      <button id="global-create-menu-anchor" aria-label="Create something new" data-target="react-partial-anchor.anchor" type="button" data-view-component="true" class="AppHeader-button global-create-button Button--secondary Button--medium Button width-auto color-fg-muted" aria-describedby="tooltip-26e98f86-8b9b-4ea3-a0d8-ecb11729eef7" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-26e98f86-8b9b-4ea3-a0d8-ecb11729eef7" for="global-create-menu-anchor" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>

      
    
        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/ui_packages_promise-with-resolvers-polyfill_promise-with-resolvers-polyfill_ts-ui_packages_re-8d43b0-7f9431d12a88.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/global-create-menu-c449421eefcc.js"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-react.0c87ead6152dce0ce7cf.module.css">

<react-partial partial-name="global-create-menu" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"createRepo":true,"importRepo":true,"codespaces":true,"spark":false,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/Oliver-JC-Li?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"Oliver-JC-Li","repo":"rag_demo"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r54:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>

      </react-partial-anchor>


          <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-0d515a7f-dc03-4811-ae95-0923d4d44e46" aria-labelledby="tooltip-acabbd22-ab07-443d-9adb-8fcc0990347d" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-acabbd22-ab07-443d-9adb-8fcc0990347d" for="icon-button-0d515a7f-dc03-4811-ae95-0923d4d44e46" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Your issues</tool-tip>

          <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-1795fd4c-a5e9-4cf7-bdde-436784c76986" aria-labelledby="tooltip-c20c1da6-ff50-407e-8575-74eab05feac7" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-c20c1da6-ff50-407e-8575-74eab05feac7" for="icon-button-1795fd4c-a5e9-4cf7-bdde-436784c76986" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Your pull requests</tool-tip>

        </div>

        <notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6NzI0NzA0MzEiLCJ0IjoxNzQ0NjczMTczfQ==--a6b78ec5b36cb469b455aea2ea2a1420c1a601dc7feffb596dbd6d5321d9c1f8" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-labelledby="notification-indicator-tooltip" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip id="notification-indicator-tooltip" data-target="notification-indicator.tooltip" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?repository_id=861863149" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
    <react-partial-anchor data-catalyst="">
  <button data-target="react-partial-anchor.anchor" data-login="Oliver-JC-Li" aria-label="Open user navigation menu" type="button" data-view-component="true" class="Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
    <span class="Button-label"><img src="./demantia_agent_demo_files/72470431" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>
  

    <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./demantia_agent_demo_files/global-user-nav-drawer-12fb192691f7.js"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/primer-react.0c87ead6152dce0ce7cf.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./demantia_agent_demo_files/global-user-nav-drawer.830d6c10c9fea7fc134e.module.css">

<react-partial partial-name="global-user-nav-drawer" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"owner":{"login":"Oliver-JC-Li","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/72470431?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2FOliver-JC-Li%2Frag_demo%2Fblob%2Fmain%2Fstop360_multiturn_rag_v2.py","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/Oliver-JC-Li?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showCopilot":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showOrganizations":true,"showSponsors":true,"showUpgrade":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false,"createMenuProps":{"createRepo":true,"importRepo":true,"codespaces":true,"spark":false,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/Oliver-JC-Li?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"Oliver-JC-Li","repo":"rag_demo"}}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r57:__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>

  </react-partial-anchor>

  </include-fragment>
</deferred-side-panel>
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


    
        <div class="AppHeader-localBar">
          <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/Oliver-JC-Li/rag_demo" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /Oliver-JC-Li/rag_demo" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/Oliver-JC-Li/rag_demo/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /Oliver-JC-Li/rag_demo/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/Oliver-JC-Li/rag_demo/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /Oliver-JC-Li/rag_demo/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/Oliver-JC-Li/rag_demo/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /Oliver-JC-Li/rag_demo/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/Oliver-JC-Li/rag_demo/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /Oliver-JC-Li/rag_demo/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/Oliver-JC-Li/rag_demo/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /Oliver-JC-Li/rag_demo/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/Oliver-JC-Li/rag_demo/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /Oliver-JC-Li/rag_demo/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="settings-tab" href="https://github.com/Oliver-JC-Li/rag_demo/settings" data-tab-item="i7settings-tab" data-selected-links="code_review_limits codespaces_repository_settings collaborators custom_tabs github_models_repo_settings hooks integration_installations interaction_limits issue_template_editor key_links_settings notifications repo_announcements repo_branch_settings repo_custom_properties repo_keys_settings repo_pages_settings repo_protected_tags_settings repo_rule_insights repo_rules_bypass_requests repo_rulesets repo_settings_copilot_coding_guidelines repo_settings_copilot_content_exclusion repo_settings reported_content repository_actions_settings_add_new_runner repository_actions_settings_general repository_actions_settings_runner_details repository_actions_settings_runners repository_actions_settings repository_environments role_details secrets_settings_actions secrets_settings_codespaces secrets_settings_dependabot secrets security_analysis security_products /Oliver-JC-Li/rag_demo/settings" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Settings&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        <span data-content="Settings">Settings</span>
          <span id="settings-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="" data-ready="true">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-09d75af2-1b9e-4d94-9b5f-bac1a041a039-button" popovertarget="action-menu-09d75af2-1b9e-4d94-9b5f-bac1a041a039-overlay" aria-controls="action-menu-09d75af2-1b9e-4d94-9b5f-bac1a041a039-list" aria-haspopup="true" aria-labelledby="tooltip-24e8db85-c7d6-4b5c-87ae-ab6dabff0d67" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-24e8db85-c7d6-4b5c-87ae-ab6dabff0d67" for="action-menu-09d75af2-1b9e-4d94-9b5f-bac1a041a039-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-09d75af2-1b9e-4d94-9b5f-bac1a041a039-overlay" anchor="action-menu-09d75af2-1b9e-4d94-9b5f-bac1a041a039-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-09d75af2-1b9e-4d94-9b5f-bac1a041a039-button" id="action-menu-09d75af2-1b9e-4d94-9b5f-bac1a041a039-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-44195475-57fa-4813-bccd-9d0d2344571b" href="https://github.com/Oliver-JC-Li/rag_demo" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-c92c8a21-32ef-4525-baf3-26d347cfd997" href="https://github.com/Oliver-JC-Li/rag_demo/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-6b856f82-f672-4167-9644-79fe1f6837e5" href="https://github.com/Oliver-JC-Li/rag_demo/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-33e63ce6-e264-4aa4-9753-8f2c63fac684" href="https://github.com/Oliver-JC-Li/rag_demo/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-1487c0e5-96bd-4fd2-952c-10328de73022" href="https://github.com/Oliver-JC-Li/rag_demo/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-c4008d66-5de8-4374-aaa5-8635bdfa4eac" href="https://github.com/Oliver-JC-Li/rag_demo/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-bc5668ce-6edf-4b80-a22f-a1383e420938" href="https://github.com/Oliver-JC-Li/rag_demo/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i7settings-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-36348aee-11c8-4cb7-aa6f-26abcb063809" href="https://github.com/Oliver-JC-Li/rag_demo/settings" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
          
        </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py">Reload</a> to refresh your session.</span>

    <button id="icon-button-3717b8bb-6c3b-40d9-b34c-68cf51643b5a" aria-labelledby="tooltip-f5e73bbc-d948-469c-95da-60bc705f84c9" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-f5e73bbc-d948-469c-95da-60bc705f84c9" for="icon-button-3717b8bb-6c3b-40d9-b34c-68cf51643b5a" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6NzI0NzA0MzEiLCJ0IjoxNzQ0NjczMTczfQ==--a6b78ec5b36cb469b455aea2ea2a1420c1a601dc7feffb596dbd6d5321d9c1f8" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/Oliver-JC-Li/rag_demo/tree/main?resume=1">Open in codespace</a>




    
      
    








<react-app app-name="react-code-view" initial-path="/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py" style="display: block; min-height: calc(100vh - 64px);" data-attempted-ssr="true" data-ssr="true" data-lazy="false" data-alternate="false" data-data-router-enabled="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":".devcontainer","path":".devcontainer","contentType":"directory"},{"name":"catt","path":"catt","contentType":"directory"},{"name":"star_c","path":"star_c","contentType":"directory"},{"name":"stop360","path":"stop360","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"catt_rag.py","path":"catt_rag.py","contentType":"file"},{"name":"requirements.txt","path":"requirements.txt","contentType":"file"},{"name":"star_c_training_manual.pdf","path":"star_c_training_manual.pdf","contentType":"file"},{"name":"stop360_conversational_v2.py","path":"stop360_conversational_v2.py","contentType":"file"},{"name":"stop360_multiturn_rag.py","path":"stop360_multiturn_rag.py","contentType":"file"},{"name":"stop360_multiturn_rag_v2.py","path":"stop360_multiturn_rag_v2.py","contentType":"file"},{"name":"stop360_rag.py","path":"stop360_rag.py","contentType":"file"}],"totalCount":12}},"fileTreeProcessingTime":3.421856,"foldersToFetch":[],"repo":{"id":861863149,"defaultBranch":"main","name":"rag_demo","ownerLogin":"Oliver-JC-Li","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2024-09-23T09:27:57.000-07:00","ownerAvatar":"https://avatars.githubusercontent.com/u/72470431?v=4","public":true,"private":false,"isOrgOwned":false},"codeLineWrapEnabled":false,"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1727108878.411154","canEdit":true,"refType":"branch","currentOid":"a2d9f6b8efc77b42fc6dab664f8ab4b036c0ac8f"},"path":"stop360_multiturn_rag_v2.py","currentUser":{"id":72470431,"login":"Oliver-JC-Li","userEmail":"oli3@uw.edu"},"blob":{"rawLines":["from langchain_community.document_loaders import PyPDFLoader","from langchain.text_splitter import RecursiveCharacterTextSplitter","from langchain_community.vectorstores import FAISS","from langchain_openai import ChatOpenAI, OpenAIEmbeddings","from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder","from langchain.chains.combine_documents import create_stuff_documents_chain","from langchain.chains.history_aware_retriever import create_history_aware_retriever","from langchain.chains.retrieval import create_retrieval_chain","from langchain_community.chat_message_histories import ChatMessageHistory","from langchain_core.chat_history import BaseChatMessageHistory","from langchain_core.runnables.history import RunnableWithMessageHistory","from langchain_core.messages import HumanMessage, AIMessage","import streamlit as st","","","openai_api_key = st.secrets[\"OPENAI_API_KEY\"]","","llm = ChatOpenAI(model='gpt-4o-mini', api_key=openai_api_key)","","# Load the documents","loader = PyPDFLoader(\"./stop360/STOP360_Template.pdf\")","docs = loader.load()","text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)","doc_chunks = text_splitter.split_documents(docs)","vector_db = FAISS.from_documents(doc_chunks, embedding=OpenAIEmbeddings())","retriever = vector_db.as_retriever()","","# Contextualize question","context_q_system_prompt = (\"\"\"","Given a chat history and the latest user question which might","reference context in the chat history, formulate a standalone","question which can be understood without the chat history. Do","NOT answer the question, just reformulate it if needed and otherwise","return it as is.","\"\"\")","","llm = ChatOpenAI(model='gpt-4o-mini')","","context_q_prompt = ChatPromptTemplate.from_messages(","    [","        (\"system\", context_q_system_prompt),","        MessagesPlaceholder(\"chat_history\"),","        (\"human\", \"{input}\")","    ]","",")","history_aware_retriever = create_history_aware_retriever(llm, retriever, context_q_prompt)","","# Question Answering","system_prompt = (\"\"\"","You are an assistant for question-answering tasks. Use the following","pieces of retrieved context to answer the question.","\u003ccontext\u003e","{context}","\u003c/context\u003e","\"\"\")","","qa_prompt = ChatPromptTemplate.from_messages(","    [","        (\"system\", system_prompt),","        MessagesPlaceholder(\"chat_history\"),","        (\"human\", \"{input}\")","    ]",")","question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)","rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)","","","# Manage chat history","chat_history = {}","","","def get_session_history(session_id: str) -\u003e BaseChatMessageHistory:","    if session_id not in chat_history:","        chat_history[session_id] = ChatMessageHistory()","    return chat_history[session_id]","","","conversational_rag_chain = RunnableWithMessageHistory(","    rag_chain,","    get_session_history,","    input_messages_key=\"input\",","    history_messages_key=\"chat_history\",","    output_messages_key=\"answer\"",")","","# Streamlit framework","vector_store = []","st.header(\"STOP360 conversational chatbot\")","","if \"chat_history\" not in st.session_state:","    st.session_state.chat_history = [","        AIMessage(content=\"I am a vertual study assistant, please as any question regarding STOP360 study\")","    ]","","if vector_store not in st.session_state:","    st.session_state.vector_store = retriever","","user_input = st.chat_input(\"Ask you question over here\")","","if user_input is not None and user_input.strip() != \"\":","    response = conversational_rag_chain.invoke(","        {'input': user_input},","        config={","            \"configurable\": {\"session_id\": \"stop360_1\"}","        }","    )['answer']","","    st.session_state.chat_history.append(HumanMessage(content=user_input))","    st.session_state.chat_history.append(AIMessage(content=response))","","for message in st.session_state.chat_history:","    if isinstance(message, AIMessage):","        with st.chat_message(\"AI\"):","            st.write(message.content)","    else:","        with st.chat_message(\"Human\"):","            st.write(message.content)"],"stylingDirectives":null,"colorizedLines":["\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain_community\u003c/span\u003e.\u003cspan class=pl-s1\u003edocument_loaders\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003ePyPDFLoader\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain\u003c/span\u003e.\u003cspan class=pl-s1\u003etext_splitter\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eRecursiveCharacterTextSplitter\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain_community\u003c/span\u003e.\u003cspan class=pl-s1\u003evectorstores\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-c1\u003eFAISS\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain_openai\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eChatOpenAI\u003c/span\u003e, \u003cspan class=pl-v\u003eOpenAIEmbeddings\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain\u003c/span\u003e.\u003cspan class=pl-s1\u003eprompts\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eChatPromptTemplate\u003c/span\u003e, \u003cspan class=pl-v\u003eMessagesPlaceholder\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain\u003c/span\u003e.\u003cspan class=pl-s1\u003echains\u003c/span\u003e.\u003cspan class=pl-s1\u003ecombine_documents\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003ecreate_stuff_documents_chain\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain\u003c/span\u003e.\u003cspan class=pl-s1\u003echains\u003c/span\u003e.\u003cspan class=pl-s1\u003ehistory_aware_retriever\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003ecreate_history_aware_retriever\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain\u003c/span\u003e.\u003cspan class=pl-s1\u003echains\u003c/span\u003e.\u003cspan class=pl-s1\u003eretrieval\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003ecreate_retrieval_chain\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain_community\u003c/span\u003e.\u003cspan class=pl-s1\u003echat_message_histories\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eChatMessageHistory\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain_core\u003c/span\u003e.\u003cspan class=pl-s1\u003echat_history\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eBaseChatMessageHistory\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain_core\u003c/span\u003e.\u003cspan class=pl-s1\u003erunnables\u003c/span\u003e.\u003cspan class=pl-s1\u003ehistory\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eRunnableWithMessageHistory\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003elangchain_core\u003c/span\u003e.\u003cspan class=pl-s1\u003emessages\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eHumanMessage\u003c/span\u003e, \u003cspan class=pl-v\u003eAIMessage\u003c/span\u003e","\u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-s1\u003estreamlit\u003c/span\u003e \u003cspan class=pl-k\u003eas\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e","","","\u003cspan class=pl-s1\u003eopenai_api_key\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esecrets\u003c/span\u003e[\u003cspan class=pl-s\u003e\u0026quot;OPENAI_API_KEY\u0026quot;\u003c/span\u003e]","","\u003cspan class=pl-s1\u003ellm\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eChatOpenAI\u003c/span\u003e(\u003cspan class=pl-s1\u003emodel\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026#39;gpt-4o-mini\u0026#39;\u003c/span\u003e, \u003cspan class=pl-s1\u003eapi_key\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s1\u003eopenai_api_key\u003c/span\u003e)","","\u003cspan class=pl-c\u003e# Load the documents\u003c/span\u003e","\u003cspan class=pl-s1\u003eloader\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003ePyPDFLoader\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;./stop360/STOP360_Template.pdf\u0026quot;\u003c/span\u003e)","\u003cspan class=pl-s1\u003edocs\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003eloader\u003c/span\u003e.\u003cspan class=pl-c1\u003eload\u003c/span\u003e()","\u003cspan class=pl-s1\u003etext_splitter\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eRecursiveCharacterTextSplitter\u003c/span\u003e(\u003cspan class=pl-s1\u003echunk_size\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-c1\u003e1000\u003c/span\u003e, \u003cspan class=pl-s1\u003echunk_overlap\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-c1\u003e20\u003c/span\u003e)","\u003cspan class=pl-s1\u003edoc_chunks\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003etext_splitter\u003c/span\u003e.\u003cspan class=pl-c1\u003esplit_documents\u003c/span\u003e(\u003cspan class=pl-s1\u003edocs\u003c/span\u003e)","\u003cspan class=pl-s1\u003evector_db\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-c1\u003eFAISS\u003c/span\u003e.\u003cspan class=pl-c1\u003efrom_documents\u003c/span\u003e(\u003cspan class=pl-s1\u003edoc_chunks\u003c/span\u003e, \u003cspan class=pl-s1\u003eembedding\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-en\u003eOpenAIEmbeddings\u003c/span\u003e())","\u003cspan class=pl-s1\u003eretriever\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003evector_db\u003c/span\u003e.\u003cspan class=pl-c1\u003eas_retriever\u003c/span\u003e()","","\u003cspan class=pl-c\u003e# Contextualize question\u003c/span\u003e","\u003cspan class=pl-s1\u003econtext_q_system_prompt\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e (\u003cspan class=pl-s\u003e\u0026quot;\u0026quot;\u0026quot;\u003c/span\u003e","\u003cspan class=pl-s\u003eGiven a chat history and the latest user question which might\u003c/span\u003e","\u003cspan class=pl-s\u003ereference context in the chat history, formulate a standalone\u003c/span\u003e","\u003cspan class=pl-s\u003equestion which can be understood without the chat history. Do\u003c/span\u003e","\u003cspan class=pl-s\u003eNOT answer the question, just reformulate it if needed and otherwise\u003c/span\u003e","\u003cspan class=pl-s\u003ereturn it as is.\u003c/span\u003e","\u003cspan class=pl-s\u003e\u0026quot;\u0026quot;\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-s1\u003ellm\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eChatOpenAI\u003c/span\u003e(\u003cspan class=pl-s1\u003emodel\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026#39;gpt-4o-mini\u0026#39;\u003c/span\u003e)","","\u003cspan class=pl-s1\u003econtext_q_prompt\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-v\u003eChatPromptTemplate\u003c/span\u003e.\u003cspan class=pl-c1\u003efrom_messages\u003c/span\u003e(","    [","        (\u003cspan class=pl-s\u003e\u0026quot;system\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s1\u003econtext_q_system_prompt\u003c/span\u003e),","        \u003cspan class=pl-en\u003eMessagesPlaceholder\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;chat_history\u0026quot;\u003c/span\u003e),","        (\u003cspan class=pl-s\u003e\u0026quot;human\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;{input}\u0026quot;\u003c/span\u003e)","    ]","",")","\u003cspan class=pl-s1\u003ehistory_aware_retriever\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003ecreate_history_aware_retriever\u003c/span\u003e(\u003cspan class=pl-s1\u003ellm\u003c/span\u003e, \u003cspan class=pl-s1\u003eretriever\u003c/span\u003e, \u003cspan class=pl-s1\u003econtext_q_prompt\u003c/span\u003e)","","\u003cspan class=pl-c\u003e# Question Answering\u003c/span\u003e","\u003cspan class=pl-s1\u003esystem_prompt\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e (\u003cspan class=pl-s\u003e\u0026quot;\u0026quot;\u0026quot;\u003c/span\u003e","\u003cspan class=pl-s\u003eYou are an assistant for question-answering tasks. Use the following\u003c/span\u003e","\u003cspan class=pl-s\u003epieces of retrieved context to answer the question.\u003c/span\u003e","\u003cspan class=pl-s\u003e\u0026lt;context\u0026gt;\u003c/span\u003e","\u003cspan class=pl-s\u003e{context}\u003c/span\u003e","\u003cspan class=pl-s\u003e\u0026lt;/context\u0026gt;\u003c/span\u003e","\u003cspan class=pl-s\u003e\u0026quot;\u0026quot;\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-s1\u003eqa_prompt\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-v\u003eChatPromptTemplate\u003c/span\u003e.\u003cspan class=pl-c1\u003efrom_messages\u003c/span\u003e(","    [","        (\u003cspan class=pl-s\u003e\u0026quot;system\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s1\u003esystem_prompt\u003c/span\u003e),","        \u003cspan class=pl-en\u003eMessagesPlaceholder\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;chat_history\u0026quot;\u003c/span\u003e),","        (\u003cspan class=pl-s\u003e\u0026quot;human\u0026quot;\u003c/span\u003e, \u003cspan class=pl-s\u003e\u0026quot;{input}\u0026quot;\u003c/span\u003e)","    ]",")","\u003cspan class=pl-s1\u003equestion_answer_chain\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003ecreate_stuff_documents_chain\u003c/span\u003e(\u003cspan class=pl-s1\u003ellm\u003c/span\u003e, \u003cspan class=pl-s1\u003eqa_prompt\u003c/span\u003e)","\u003cspan class=pl-s1\u003erag_chain\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003ecreate_retrieval_chain\u003c/span\u003e(\u003cspan class=pl-s1\u003ehistory_aware_retriever\u003c/span\u003e, \u003cspan class=pl-s1\u003equestion_answer_chain\u003c/span\u003e)","","","\u003cspan class=pl-c\u003e# Manage chat history\u003c/span\u003e","\u003cspan class=pl-s1\u003echat_history\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e {}","","","\u003cspan class=pl-k\u003edef\u003c/span\u003e \u003cspan class=pl-en\u003eget_session_history\u003c/span\u003e(\u003cspan class=pl-s1\u003esession_id\u003c/span\u003e: \u003cspan class=pl-smi\u003estr\u003c/span\u003e) \u003cspan class=pl-c1\u003e-\u0026gt;\u003c/span\u003e \u003cspan class=pl-smi\u003eBaseChatMessageHistory\u003c/span\u003e:","    \u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s1\u003esession_id\u003c/span\u003e \u003cspan class=pl-c1\u003e\u003cspan class=pl-c1\u003enot\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e\u003c/span\u003e \u003cspan class=pl-s1\u003echat_history\u003c/span\u003e:","        \u003cspan class=pl-s1\u003echat_history\u003c/span\u003e[\u003cspan class=pl-s1\u003esession_id\u003c/span\u003e] \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eChatMessageHistory\u003c/span\u003e()","    \u003cspan class=pl-k\u003ereturn\u003c/span\u003e \u003cspan class=pl-s1\u003echat_history\u003c/span\u003e[\u003cspan class=pl-s1\u003esession_id\u003c/span\u003e]","","","\u003cspan class=pl-s1\u003econversational_rag_chain\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eRunnableWithMessageHistory\u003c/span\u003e(","    \u003cspan class=pl-s1\u003erag_chain\u003c/span\u003e,","    \u003cspan class=pl-s1\u003eget_session_history\u003c/span\u003e,","    \u003cspan class=pl-s1\u003einput_messages_key\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;input\u0026quot;\u003c/span\u003e,","    \u003cspan class=pl-s1\u003ehistory_messages_key\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;chat_history\u0026quot;\u003c/span\u003e,","    \u003cspan class=pl-s1\u003eoutput_messages_key\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;answer\u0026quot;\u003c/span\u003e",")","","\u003cspan class=pl-c\u003e# Streamlit framework\u003c/span\u003e","\u003cspan class=pl-s1\u003evector_store\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e []","\u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003eheader\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;STOP360 conversational chatbot\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s\u003e\u0026quot;chat_history\u0026quot;\u003c/span\u003e \u003cspan class=pl-c1\u003e\u003cspan class=pl-c1\u003enot\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esession_state\u003c/span\u003e:","    \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esession_state\u003c/span\u003e.\u003cspan class=pl-c1\u003echat_history\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e [","        \u003cspan class=pl-en\u003eAIMessage\u003c/span\u003e(\u003cspan class=pl-s1\u003econtent\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;I am a vertual study assistant, please as any question regarding STOP360 study\u0026quot;\u003c/span\u003e)","    ]","","\u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s1\u003evector_store\u003c/span\u003e \u003cspan class=pl-c1\u003e\u003cspan class=pl-c1\u003enot\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esession_state\u003c/span\u003e:","    \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esession_state\u003c/span\u003e.\u003cspan class=pl-c1\u003evector_store\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003eretriever\u003c/span\u003e","","\u003cspan class=pl-s1\u003euser_input\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003echat_input\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Ask you question over here\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-s1\u003euser_input\u003c/span\u003e \u003cspan class=pl-c1\u003e\u003cspan class=pl-c1\u003eis\u003c/span\u003e \u003cspan class=pl-c1\u003enot\u003c/span\u003e\u003c/span\u003e \u003cspan class=pl-c1\u003eNone\u003c/span\u003e \u003cspan class=pl-c1\u003eand\u003c/span\u003e \u003cspan class=pl-s1\u003euser_input\u003c/span\u003e.\u003cspan class=pl-c1\u003estrip\u003c/span\u003e() \u003cspan class=pl-c1\u003e!=\u003c/span\u003e \u003cspan class=pl-s\u003e\u0026quot;\u0026quot;\u003c/span\u003e:","    \u003cspan class=pl-s1\u003eresponse\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-s1\u003econversational_rag_chain\u003c/span\u003e.\u003cspan class=pl-c1\u003einvoke\u003c/span\u003e(","        {\u003cspan class=pl-s\u003e\u0026#39;input\u0026#39;\u003c/span\u003e: \u003cspan class=pl-s1\u003euser_input\u003c/span\u003e},","        \u003cspan class=pl-s1\u003econfig\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e{","            \u003cspan class=pl-s\u003e\u0026quot;configurable\u0026quot;\u003c/span\u003e: {\u003cspan class=pl-s\u003e\u0026quot;session_id\u0026quot;\u003c/span\u003e: \u003cspan class=pl-s\u003e\u0026quot;stop360_1\u0026quot;\u003c/span\u003e}","        }","    )[\u003cspan class=pl-s\u003e\u0026#39;answer\u0026#39;\u003c/span\u003e]","","    \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esession_state\u003c/span\u003e.\u003cspan class=pl-c1\u003echat_history\u003c/span\u003e.\u003cspan class=pl-c1\u003eappend\u003c/span\u003e(\u003cspan class=pl-en\u003eHumanMessage\u003c/span\u003e(\u003cspan class=pl-s1\u003econtent\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s1\u003euser_input\u003c/span\u003e))","    \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esession_state\u003c/span\u003e.\u003cspan class=pl-c1\u003echat_history\u003c/span\u003e.\u003cspan class=pl-c1\u003eappend\u003c/span\u003e(\u003cspan class=pl-en\u003eAIMessage\u003c/span\u003e(\u003cspan class=pl-s1\u003econtent\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s1\u003eresponse\u003c/span\u003e))","","\u003cspan class=pl-k\u003efor\u003c/span\u003e \u003cspan class=pl-s1\u003emessage\u003c/span\u003e \u003cspan class=pl-c1\u003ein\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003esession_state\u003c/span\u003e.\u003cspan class=pl-c1\u003echat_history\u003c/span\u003e:","    \u003cspan class=pl-k\u003eif\u003c/span\u003e \u003cspan class=pl-en\u003eisinstance\u003c/span\u003e(\u003cspan class=pl-s1\u003emessage\u003c/span\u003e, \u003cspan class=pl-v\u003eAIMessage\u003c/span\u003e):","        \u003cspan class=pl-k\u003ewith\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003echat_message\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;AI\u0026quot;\u003c/span\u003e):","            \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003ewrite\u003c/span\u003e(\u003cspan class=pl-s1\u003emessage\u003c/span\u003e.\u003cspan class=pl-c1\u003econtent\u003c/span\u003e)","    \u003cspan class=pl-k\u003eelse\u003c/span\u003e:","        \u003cspan class=pl-k\u003ewith\u003c/span\u003e \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003echat_message\u003c/span\u003e(\u003cspan class=pl-s\u003e\u0026quot;Human\u0026quot;\u003c/span\u003e):","            \u003cspan class=pl-s1\u003est\u003c/span\u003e.\u003cspan class=pl-c1\u003ewrite\u003c/span\u003e(\u003cspan class=pl-s1\u003emessage\u003c/span\u003e.\u003cspan class=pl-c1\u003econtent\u003c/span\u003e)"],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Oliver-JC-Li/rag_demo/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"stop360_multiturn_rag_v2.py","displayUrl":"https://github.com/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py?raw=true","headerInfo":{"blobSize":"3.86 KB","deleteTooltip":"Delete this file","editTooltip":"Edit this file","ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"onBranch":true,"shortPath":"3756d59","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FOliver-JC-Li%2Frag_demo%2Fblob%2Fmain%2Fstop360_multiturn_rag_v2.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"118","truncatedSloc":"95"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Oliver-JC-Li/rag_demo/blob/main/stop360_multiturn_rag_v2.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/Oliver-JC-Li/rag_demo/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/Oliver-JC-Li/rag_demo/raw/refs/heads/main/stop360_multiturn_rag_v2.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"openai_api_key","kind":"constant","ident_start":823,"ident_end":837,"extent_start":823,"extent_end":868,"fully_qualified_name":"openai_api_key","ident_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":15,"utf16_col":14}},"extent_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":15,"utf16_col":45}}},{"name":"llm","kind":"constant","ident_start":870,"ident_end":873,"extent_start":870,"extent_end":931,"fully_qualified_name":"llm","ident_utf16":{"start":{"line_number":17,"utf16_col":0},"end":{"line_number":17,"utf16_col":3}},"extent_utf16":{"start":{"line_number":17,"utf16_col":0},"end":{"line_number":17,"utf16_col":61}}},{"name":"loader","kind":"constant","ident_start":954,"ident_end":960,"extent_start":954,"extent_end":1008,"fully_qualified_name":"loader","ident_utf16":{"start":{"line_number":20,"utf16_col":0},"end":{"line_number":20,"utf16_col":6}},"extent_utf16":{"start":{"line_number":20,"utf16_col":0},"end":{"line_number":20,"utf16_col":54}}},{"name":"docs","kind":"constant","ident_start":1009,"ident_end":1013,"extent_start":1009,"extent_end":1029,"fully_qualified_name":"docs","ident_utf16":{"start":{"line_number":21,"utf16_col":0},"end":{"line_number":21,"utf16_col":4}},"extent_utf16":{"start":{"line_number":21,"utf16_col":0},"end":{"line_number":21,"utf16_col":20}}},{"name":"text_splitter","kind":"constant","ident_start":1030,"ident_end":1043,"extent_start":1030,"extent_end":1111,"fully_qualified_name":"text_splitter","ident_utf16":{"start":{"line_number":22,"utf16_col":0},"end":{"line_number":22,"utf16_col":13}},"extent_utf16":{"start":{"line_number":22,"utf16_col":0},"end":{"line_number":22,"utf16_col":81}}},{"name":"doc_chunks","kind":"constant","ident_start":1112,"ident_end":1122,"extent_start":1112,"extent_end":1160,"fully_qualified_name":"doc_chunks","ident_utf16":{"start":{"line_number":23,"utf16_col":0},"end":{"line_number":23,"utf16_col":10}},"extent_utf16":{"start":{"line_number":23,"utf16_col":0},"end":{"line_number":23,"utf16_col":48}}},{"name":"vector_db","kind":"constant","ident_start":1161,"ident_end":1170,"extent_start":1161,"extent_end":1235,"fully_qualified_name":"vector_db","ident_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":24,"utf16_col":9}},"extent_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":24,"utf16_col":74}}},{"name":"retriever","kind":"constant","ident_start":1236,"ident_end":1245,"extent_start":1236,"extent_end":1272,"fully_qualified_name":"retriever","ident_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":25,"utf16_col":9}},"extent_utf16":{"start":{"line_number":25,"utf16_col":0},"end":{"line_number":25,"utf16_col":36}}},{"name":"context_q_system_prompt","kind":"constant","ident_start":1299,"ident_end":1322,"extent_start":1299,"extent_end":1606,"fully_qualified_name":"context_q_system_prompt","ident_utf16":{"start":{"line_number":28,"utf16_col":0},"end":{"line_number":28,"utf16_col":23}},"extent_utf16":{"start":{"line_number":28,"utf16_col":0},"end":{"line_number":34,"utf16_col":4}}},{"name":"llm","kind":"constant","ident_start":1608,"ident_end":1611,"extent_start":1608,"extent_end":1645,"fully_qualified_name":"llm","ident_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":3}},"extent_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":37}}},{"name":"context_q_prompt","kind":"constant","ident_start":1647,"ident_end":1663,"extent_start":1647,"extent_end":1833,"fully_qualified_name":"context_q_prompt","ident_utf16":{"start":{"line_number":38,"utf16_col":0},"end":{"line_number":38,"utf16_col":16}},"extent_utf16":{"start":{"line_number":38,"utf16_col":0},"end":{"line_number":45,"utf16_col":1}}},{"name":"history_aware_retriever","kind":"constant","ident_start":1834,"ident_end":1857,"extent_start":1834,"extent_end":1924,"fully_qualified_name":"history_aware_retriever","ident_utf16":{"start":{"line_number":46,"utf16_col":0},"end":{"line_number":46,"utf16_col":23}},"extent_utf16":{"start":{"line_number":46,"utf16_col":0},"end":{"line_number":46,"utf16_col":90}}},{"name":"system_prompt","kind":"constant","ident_start":1947,"ident_end":1960,"extent_start":1947,"extent_end":2124,"fully_qualified_name":"system_prompt","ident_utf16":{"start":{"line_number":49,"utf16_col":0},"end":{"line_number":49,"utf16_col":13}},"extent_utf16":{"start":{"line_number":49,"utf16_col":0},"end":{"line_number":55,"utf16_col":4}}},{"name":"qa_prompt","kind":"constant","ident_start":2126,"ident_end":2135,"extent_start":2126,"extent_end":2294,"fully_qualified_name":"qa_prompt","ident_utf16":{"start":{"line_number":57,"utf16_col":0},"end":{"line_number":57,"utf16_col":9}},"extent_utf16":{"start":{"line_number":57,"utf16_col":0},"end":{"line_number":63,"utf16_col":1}}},{"name":"question_answer_chain","kind":"constant","ident_start":2295,"ident_end":2316,"extent_start":2295,"extent_end":2363,"fully_qualified_name":"question_answer_chain","ident_utf16":{"start":{"line_number":64,"utf16_col":0},"end":{"line_number":64,"utf16_col":21}},"extent_utf16":{"start":{"line_number":64,"utf16_col":0},"end":{"line_number":64,"utf16_col":68}}},{"name":"rag_chain","kind":"constant","ident_start":2364,"ident_end":2373,"extent_start":2364,"extent_end":2446,"fully_qualified_name":"rag_chain","ident_utf16":{"start":{"line_number":65,"utf16_col":0},"end":{"line_number":65,"utf16_col":9}},"extent_utf16":{"start":{"line_number":65,"utf16_col":0},"end":{"line_number":65,"utf16_col":82}}},{"name":"chat_history","kind":"constant","ident_start":2471,"ident_end":2483,"extent_start":2471,"extent_end":2488,"fully_qualified_name":"chat_history","ident_utf16":{"start":{"line_number":69,"utf16_col":0},"end":{"line_number":69,"utf16_col":12}},"extent_utf16":{"start":{"line_number":69,"utf16_col":0},"end":{"line_number":69,"utf16_col":17}}},{"name":"get_session_history","kind":"function","ident_start":2495,"ident_end":2514,"extent_start":2491,"extent_end":2689,"fully_qualified_name":"get_session_history","ident_utf16":{"start":{"line_number":72,"utf16_col":4},"end":{"line_number":72,"utf16_col":23}},"extent_utf16":{"start":{"line_number":72,"utf16_col":0},"end":{"line_number":75,"utf16_col":35}}},{"name":"conversational_rag_chain","kind":"constant","ident_start":2692,"ident_end":2716,"extent_start":2692,"extent_end":2894,"fully_qualified_name":"conversational_rag_chain","ident_utf16":{"start":{"line_number":78,"utf16_col":0},"end":{"line_number":78,"utf16_col":24}},"extent_utf16":{"start":{"line_number":78,"utf16_col":0},"end":{"line_number":84,"utf16_col":1}}},{"name":"vector_store","kind":"constant","ident_start":2918,"ident_end":2930,"extent_start":2918,"extent_end":2935,"fully_qualified_name":"vector_store","ident_utf16":{"start":{"line_number":87,"utf16_col":0},"end":{"line_number":87,"utf16_col":12}},"extent_utf16":{"start":{"line_number":87,"utf16_col":0},"end":{"line_number":87,"utf16_col":17}}},{"name":"user_input","kind":"constant","ident_start":3265,"ident_end":3275,"extent_start":3265,"extent_end":3321,"fully_qualified_name":"user_input","ident_utf16":{"start":{"line_number":98,"utf16_col":0},"end":{"line_number":98,"utf16_col":10}},"extent_utf16":{"start":{"line_number":98,"utf16_col":0},"end":{"line_number":98,"utf16_col":56}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"modelsAccessAllowed":true,"modelsRepoIntegrationEnabled":false,"csrf_tokens":{"/Oliver-JC-Li/rag_demo/branches":{"post":"ls1x-v709bhTpnUerGQYefC3C1enhZCmI63UHMfjozzqKE4pJnWp7_ceP7Jz9JzaZ6rab74NGKi9FshZSO9v5g"},"/repos/preferences":{"post":"V-dYGElHcdgR32uJmTed0lksLlHrItFaBnlHZOL115OZu7hWF2lHzAYFrq5XyO-vV-_BxaOEUkrMbwSU_NY8cg"}}},"title":"rag_demo/stop360_multiturn_rag_v2.py at main · Oliver-JC-Li/rag_demo","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-7d7eb7c71814.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-708ec8ade250.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"react_blob_overlay":true,"accessible_code_button":true,"github_models_repo_integration":false}}}</script>
  <div data-target="react-app.reactRoot"><meta data-hydrostats="publish"> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="y,Shift+Y"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div><div style="--sticky-pane-height: calc(100vh - (max(0px, 0px))); --spacing: var(--spacing-none);" class="Box-sc-g0xbh4-0 prc-PageLayout-PageLayoutRoot-1zlEO"><div class="Box-sc-g0xbh4-0 prc-PageLayout-PageLayoutWrapper-s2ao4" data-width="full"><div class="Box-sc-g0xbh4-0 prc-PageLayout-PageLayoutContent-jzDMn"><div tabindex="0" class="Box-sc-g0xbh4-0 gISSDQ"><div class="Box-sc-g0xbh4-0 prc-PageLayout-PaneWrapper-nGO0U ReposFileTreePane-module__Pane--wS7IV ReposFileTreePane-module__HideTree--zU_Nd ReposFileTreePane-module__HidePaneWithTreeOverlay--fHI8k" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="start" data-sticky="true"><div class="Box-sc-g0xbh4-0 prc-PageLayout-HorizontalDivider-CYLp5 prc-PageLayout-PaneHorizontalDivider-4exOb" data-variant="none" data-position="start" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="Box-sc-g0xbh4-0 prc-PageLayout-Pane-Vl5LI" data-resizable="true" style="--spacing:var(--spacing-none);--pane-min-width:256px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));--pane-width-size:var(--pane-width-large);--pane-width:320px"></div><div class="Box-sc-g0xbh4-0 prc-PageLayout-VerticalDivider-4A4Qm prc-PageLayout-PaneVerticalDivider-1c9vy" data-variant="line" data-position="start" style="--spacing:var(--spacing-none)"><div role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="411" aria-valuenow="0" aria-valuetext="Pane width 0 pixels" tabindex="0" class="Box-sc-g0xbh4-0 fFMzrG"></div></div></div></div><div class="Box-sc-g0xbh4-0 prc-PageLayout-ContentWrapper-b-QRo CodeView-module__SplitPageLayout_Content--qxR1C" data-is-hidden="false"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 prc-PageLayout-Content--F7-I" data-width="full" style="--spacing:var(--spacing-none)"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 leYMvG"><div class="Box-sc-g0xbh4-0 KMPzq"><div class="Box-sc-g0xbh4-0 hfKjHv container"><div class="px-3 pt-3 pb-0" id="StickyHeader"><div class="Box-sc-g0xbh4-0 gZWyZE"><div class="Box-sc-g0xbh4-0 dwYKDk"><div class="Box-sc-g0xbh4-0 ibcGmb react-code-view-header-wrap--narrow"><div class="Box-sc-g0xbh4-0 hKaEJF"><h2 class="Box-sc-g0xbh4-0 XosP prc-Heading-Heading-6CmGO"><button type="button" aria-label="Expand file tree" data-hotkey="Meta+b" data-testid="expand-file-tree-button-mobile" class="Box-sc-g0xbh4-0 hMLRgO prc-Button-ButtonBase-c50BI" data-loading="false" data-size="medium" data-variant="invisible" aria-describedby=":r4i:-loading-announcement" style="--button-color: fg.muted;"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Files</span></span></button><span role="tooltip" aria-label="Expand file tree" id="expand-button-file-tree-button" class="Tooltip__TooltipBase-sc-17tf59c-0 fiSvBN tooltipped-se"><button data-component="IconButton" type="button" data-testid="expand-file-tree-button" aria-expanded="false" aria-controls="repos-file-tree" data-hotkey="Meta+b" data-analytics-opt-out="true" class="prc-Button-ButtonBase-c50BI react-tree-toggle-button-with-indicator position-relative ExpandFileTreeButton-module__expandButton--gL4is ExpandFileTreeButton-module__filesButtonBreakpoint--WfX9t fgColor-muted prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":r4k:-loading-announcement" aria-labelledby="expand-button-file-tree-button"><svg aria-hidden="true" focusable="false" class="octicon octicon-sidebar-collapse" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6.823 7.823a.25.25 0 0 1 0 .354l-2.396 2.396A.25.25 0 0 1 4 10.396V5.604a.25.25 0 0 1 .427-.177Z"></path><path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25H9.5v-13H1.75a.25.25 0 0 0-.25.25ZM11 14.5h3.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11Z"></path></svg></button></span><button hidden="" data-testid="" data-hotkey="Meta+b" data-hotkey-scope="read-only-cursor-text-area"></button></h2></div><div class="react-code-view-header-mb--narrow mr-2"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" data-hotkey="w" aria-label="main branch" data-testid="anchor-button" class="Box-sc-g0xbh4-0 gKSEMU prc-Button-ButtonBase-c50BI ref-selector-class" data-loading="false" data-size="medium" data-variant="default" aria-describedby="branch-picker-repos-header-ref-selector-wide-loading-announcement" id="branch-picker-repos-header-ref-selector-wide"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x"><div class="Box-sc-g0xbh4-0 bZBlpz"><div class="Box-sc-g0xbh4-0 bJjzmO"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 dbrgmi ref-selector-button-text-container"><span class="Box-sc-g0xbh4-0 bmcJak prc-Text-Text-0ima0">&nbsp;main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey="w" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="Box-sc-g0xbh4-0 dHJiml react-code-view-header-mb--narrow"><div class="Box-sc-g0xbh4-0 cEytCf"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-heading" id="repos-header-breadcrumb" class="Box-sc-g0xbh4-0 fzFXnm"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="repos-header-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 iMnkmv"><li class="Box-sc-g0xbh4-0 ghzDag"><a class="Box-sc-g0xbh4-0 kHuKdh prc-Link-Link-85e08" sx="[object Object]" data-testid="breadcrumbs-repo-link" href="https://github.com/Oliver-JC-Li/rag_demo/tree/main">rag_demo</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 ghzDag"><span class="Box-sc-g0xbh4-0 hXyrdx prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 class="Box-sc-g0xbh4-0 jGhzSQ prc-Heading-Heading-6CmGO" tabindex="-1" id="file-name-id">stop360_multiturn_rag_v2.py</h1></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI ml-2 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":r4p:-loading-announcement" aria-labelledby=":r4n:"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="CopyToClipboardButton-module__tooltip--Dq1IB prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-label="Copy path" aria-hidden="true" id=":r4n:" popover="auto">Copy path</span></div></div></div><div class="react-code-view-header-element--wide"><div class="Box-sc-g0xbh4-0 faNtbn"><div class="d-flex gap-2"> <div><div class="Box-sc-g0xbh4-0 fmQaBv"><span class="Box-sc-g0xbh4-0 vcvyP TextInput-wrapper prc-components-TextInputWrapper-i1ofR prc-components-TextInputBaseWrapper-ueK9q" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id=":r4q:" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby=":r4q: :r4r:" data-component="input" class="prc-components-Input-Ic-y8" value=""><span class="TextInput-icon" id=":r4r:" aria-hidden="true"><div class="Box-sc-g0xbh4-0 dItACB"><kbd>t</kbd></div></span></span></div><button hidden="" data-testid="" data-hotkey="t,Shift+T" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="t,Shift+T"></button></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="l,Shift+L"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Mod+Alt+g"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" class="Box-sc-g0xbh4-0 dwNhzn prc-Button-ButtonBase-c50BI" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R5a6d9lab:-loading-announcement" data-hotkey="b,Shift+B,Meta+/ Meta+b"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Meta+/ Meta+b"></button><button data-component="IconButton" type="button" aria-label="More file actions" title="More file actions" data-testid="more-file-actions-button-nav-menu-wide" aria-haspopup="true" aria-expanded="false" tabindex="0" class="Box-sc-g0xbh4-0 kVRliy prc-Button-ButtonBase-c50BI js-blob-dropdown-click prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R2a6d9lab:-loading-announcement" id=":R2a6d9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div><div class="react-code-view-header-element--narrow"><div class="Box-sc-g0xbh4-0 faNtbn"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="l,Shift+L"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Mod+Alt+g"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" class="Box-sc-g0xbh4-0 dwNhzn prc-Button-ButtonBase-c50BI" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R5a7d9lab:-loading-announcement" data-hotkey="b,Shift+B,Meta+/ Meta+b"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Meta+/ Meta+b"></button><button data-component="IconButton" type="button" aria-label="More file actions" title="More file actions" data-testid="more-file-actions-button-nav-menu-narrow" aria-haspopup="true" aria-expanded="false" tabindex="0" class="Box-sc-g0xbh4-0 kVRliy prc-Button-ButtonBase-c50BI js-blob-dropdown-click prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R2a7d9lab:-loading-announcement" id=":R2a7d9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 dJxjrT react-code-view-bottom-padding"> <div class="Box-sc-g0xbh4-0 eFxKDQ"></div> <!-- --> <!-- --> </div><div class="Box-sc-g0xbh4-0 dJxjrT"> <!-- --> <!-- --> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="r,Shift+R"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="d-flex flex-column border rounded-2 mb-3 pl-1"><div class="Box-sc-g0xbh4-0 dzCJzi"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="Box-sc-g0xbh4-0 ePWWCk"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/Oliver-JC-Li" data-testid="avatar-icon-link" data-hovercard-url="/users/Oliver-JC-Li/hovercard"><img data-component="Avatar" class="Box-sc-g0xbh4-0 cvdqJW prc-Avatar-Avatar-ZRS-m" alt="Oliver-JC-Li" width="20" height="20" src="./demantia_agent_demo_files/72470431(1)" data-testid="github-avatar" aria-label="Oliver-JC-Li" style="--avatarSize-regular: 20px;"></a><a class="Box-sc-g0xbh4-0 kJvqaq prc-Link-Link-85e08" data-muted="true" href="https://github.com/Oliver-JC-Li/rag_demo/commits?author=Oliver-JC-Li" aria-label="commits by Oliver-JC-Li" data-hovercard-url="/users/Oliver-JC-Li/hovercard">Oliver-JC-Li</a></div><span class=""></span></div><div class="Box-sc-g0xbh4-0 erEOeb d-none d-sm-flex"><div class="Truncate flex-items-center f5"><span class="Truncate-text prc-Text-Text-0ima0" data-testid="latest-commit-html"><a href="https://github.com/Oliver-JC-Li/rag_demo/commit/994ad17126451ccfd265fb7e3a54eaae83f608ee" class="Link--secondary" data-pjax="true" data-hovercard-url="/Oliver-JC-Li/rag_demo/commit/994ad17126451ccfd265fb7e3a54eaae83f608ee/hovercard">Revise the file path</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time class="sc-aXZVg" tense="past" datetime="2024-10-08T20:19:44.000Z" title="Oct 8, 2024, 1:19 PM PDT"><template shadowrootmode="open">6 months ago</template>Oct 8, 2024</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-85e08" aria-label="Commit 994ad17" data-hovercard-url="/Oliver-JC-Li/rag_demo/commit/994ad17126451ccfd265fb7e3a54eaae83f608ee/hovercard" href="https://github.com/Oliver-JC-Li/rag_demo/commit/994ad17126451ccfd265fb7e3a54eaae83f608ee">994ad17</a>&nbsp;·&nbsp;<relative-time class="sc-aXZVg" tense="past" datetime="2024-10-08T20:19:44.000Z" title="Oct 8, 2024, 1:19 PM PDT"><template shadowrootmode="open">6 months ago</template>Oct 8, 2024</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">History</h2><a href="https://github.com/Oliver-JC-Li/rag_demo/commits/main/stop360_multiturn_rag_v2.py" class="prc-Button-ButtonBase-c50BI d-none d-lg-flex LinkButton-module__code-view-link-button--xvCGA flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R5dlal9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x"><span class="fgColor-default">History</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-label="Open commit details" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="Box-sc-g0xbh4-0 fvaGIa prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":r58:-loading-announcement"><svg aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button></div><div class="d-flex d-lg-none"><span role="tooltip" aria-label="History" id="history-icon-button-tooltip" class="Tooltip__TooltipBase-sc-17tf59c-0 fiSvBN tooltipped-n"><a href="https://github.com/Oliver-JC-Li/rag_demo/commits/main/stop360_multiturn_rag_v2.py" class="prc-Button-ButtonBase-c50BI LinkButton-module__code-view-link-button--xvCGA flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":Rpdlal9lab:-loading-announcement history-icon-button-tooltip"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div></div></div><div class="Box-sc-g0xbh4-0 ldRxiI"><div class="Box-sc-g0xbh4-0 fVkfyA container"><div class="Box-sc-g0xbh4-0 gNAmSV react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 jNEwzY react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 ifyOQK text-mono"><div title="3.86 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 eAtkQz"><span>118 lines (95 loc) · 3.86 KB</span></div></div></div><div class="react-code-size-details-banner"><button style="--button-color:fg.default" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="Box-sc-g0xbh4-0 jlVuVO prc-Button-ButtonBase-c50BI" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R15tal9lab:-loading-announcement" id=":R15tal9lab:"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 jdLMhu react-blob-view-header-sticky" id="repos-sticky-header"><div class="Box-sc-g0xbh4-0 tOISc"><div class="react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 jodZGf"><div class="Box-sc-g0xbh4-0 bDVoEr"><div class="Box-sc-g0xbh4-0 kYLlPM"><h2 class="Box-sc-g0xbh4-0 XosP prc-Heading-Heading-6CmGO"><button type="button" aria-label="Expand file tree" data-hotkey="Meta+b" data-testid="expand-file-tree-button-mobile" class="Box-sc-g0xbh4-0 hMLRgO prc-Button-ButtonBase-c50BI" data-loading="false" data-size="medium" data-variant="invisible" aria-describedby=":r5a:-loading-announcement" style="--button-color: fg.muted;"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Files</span></span></button><span role="tooltip" aria-label="Expand file tree" id="expand-button-file-tree-button" class="Tooltip__TooltipBase-sc-17tf59c-0 fiSvBN tooltipped-se"><button data-component="IconButton" type="button" data-testid="expand-file-tree-button" aria-expanded="false" aria-controls="repos-file-tree" data-hotkey="Meta+b" data-analytics-opt-out="true" class="prc-Button-ButtonBase-c50BI react-tree-toggle-button-with-indicator position-relative ExpandFileTreeButton-module__expandButton--gL4is ExpandFileTreeButton-module__filesButtonBreakpoint--WfX9t fgColor-muted prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":r5c:-loading-announcement" aria-labelledby="expand-button-file-tree-button"><svg aria-hidden="true" focusable="false" class="octicon octicon-sidebar-collapse" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6.823 7.823a.25.25 0 0 1 0 .354l-2.396 2.396A.25.25 0 0 1 4 10.396V5.604a.25.25 0 0 1 .427-.177Z"></path><path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25H9.5v-13H1.75a.25.25 0 0 0-.25.25ZM11 14.5h3.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11Z"></path></svg></button></span><button hidden="" data-testid="" data-hotkey="Meta+b" data-hotkey-scope="read-only-cursor-text-area"></button></h2><div class="Box-sc-g0xbh4-0 gYjEmn"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" data-hotkey="w" aria-label="main branch" data-testid="anchor-button" class="Box-sc-g0xbh4-0 gKSEMU prc-Button-ButtonBase-c50BI ref-selector-class" data-loading="false" data-size="medium" data-variant="default" aria-describedby="branch-picker-repos-header-ref-selector-loading-announcement" id="branch-picker-repos-header-ref-selector"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x"><div class="Box-sc-g0xbh4-0 bZBlpz"><div class="Box-sc-g0xbh4-0 bJjzmO"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 dbrgmi ref-selector-button-text-container"><span class="Box-sc-g0xbh4-0 bmcJak prc-Text-Text-0ima0">&nbsp;main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey="w" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="Box-sc-g0xbh4-0 kGqOLL"><div class="Box-sc-g0xbh4-0 fHind"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 fzFXnm"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 iMnkmv"><li class="Box-sc-g0xbh4-0 ghzDag"><a class="Box-sc-g0xbh4-0 kHuKdh prc-Link-Link-85e08" sx="[object Object]" data-testid="breadcrumbs-repo-link" href="https://github.com/Oliver-JC-Li/rag_demo/tree/main">rag_demo</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 ghzDag"><span class="Box-sc-g0xbh4-0 bQeXnn prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 class="Box-sc-g0xbh4-0 dnZoUW prc-Heading-Heading-6CmGO" tabindex="-1" id="sticky-file-name-id">stop360_multiturn_rag_v2.py</h1></div></div></div></div><button style="--button-color:fg.default" type="button" class="Box-sc-g0xbh4-0 dpNnZU prc-Button-ButtonBase-c50BI" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":Riptal9lab:-loading-announcement"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 cOgqet"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vW4Cq prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">File metadata and controls</h2><div class="Box-sc-g0xbh4-0 iNMjfP"><ul aria-label="File view" class="Box-sc-g0xbh4-0 gtTaSn prc-SegmentedControl-SegmentedControl-e7570" data-size="small"><li class="Box-sc-g0xbh4-0 dXYHoy prc-SegmentedControl-Item-7Aq6h" data-selected="true"><button aria-current="true" class="prc-SegmentedControl-Button-ojWXD" type="button" data-hotkey="Meta+/ Meta+c"><span class="prc-SegmentedControl-Content-gnQ4n"><div class="Box-sc-g0xbh4-0 prc-SegmentedControl-Text-c5gSh" data-text="Code">Code</div></span></button></li><li class="Box-sc-g0xbh4-0 lcvxdn prc-SegmentedControl-Item-7Aq6h"><button aria-current="false" class="prc-SegmentedControl-Button-ojWXD" type="button" data-hotkey="b,Shift+B,Meta+/ Meta+b"><span class="prc-SegmentedControl-Content-gnQ4n"><div class="Box-sc-g0xbh4-0 prc-SegmentedControl-Text-c5gSh" data-text="Blame">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Meta+/ Meta+c"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Meta+/ Meta+b"></button><div class="Box-sc-g0xbh4-0 jNEwzY react-code-size-details-in-header"><div class="Box-sc-g0xbh4-0 ifyOQK text-mono"><div title="3.86 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 eAtkQz"><span>118 lines (95 loc) · 3.86 KB</span></div></div></div><div class="react-code-size-details-in-header"><button style="--button-color:fg.default" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="Box-sc-g0xbh4-0 jlVuVO prc-Button-ButtonBase-c50BI" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R3kptal9lab:-loading-announcement" id=":R3kptal9lab:"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 kcLCKF"><button hidden="" data-testid="" data-hotkey="Meta+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Meta+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Meta+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Meta+Shift+&lt;"></button><div class="Box-sc-g0xbh4-0 kVWtTz react-blob-header-edit-and-raw-actions"><div class="Box-sc-g0xbh4-0 prc-ButtonGroup-ButtonGroup-vcMeG"><div><a href="https://github.com/Oliver-JC-Li/rag_demo/raw/refs/heads/main/stop360_multiturn_rag_v2.py" data-testid="raw-button" class="Box-sc-g0xbh4-0 gWqxTd prc-Button-ButtonBase-c50BI" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R5csptal9lab:-loading-announcement" data-hotkey="Meta+/ Meta+r"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Raw</span></span></a></div><div><button data-component="IconButton" type="button" aria-label="Copy raw content" data-testid="copy-raw-button" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rpcsptal9lab:-loading-announcement" data-hotkey="Meta+Shift+C"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div><div><span role="tooltip" aria-label="Download raw file" id=":Rdcsptal9lab:" class="Tooltip__TooltipBase-sc-17tf59c-0 fiSvBN tooltipped-n"><button data-component="IconButton" type="button" aria-label="Download raw content" data-testid="download-raw-button" class="Box-sc-g0xbh4-0 ivobqY prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rtcsptal9lab:-loading-announcement" data-hotkey="Meta+Shift+S"><svg aria-hidden="true" focusable="false" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button></span></div></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Meta+/ Meta+r"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Meta+Shift+C"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Meta+Shift+S"></button><a class="js-github-dev-shortcut d-none prc-Link-Link-85e08" href="https://github.dev/" data-hotkey="., Meta+Shift+/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="., Meta+Shift+/"></button><a class="js-github-dev-new-tab-shortcut d-none prc-Link-Link-85e08" href="https://github.dev/" target="_blank" data-hotkey="Shift+.,Shift+&gt;,&gt;"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Shift+.,Shift+&gt;,&gt;"></button><div class="Box-sc-g0xbh4-0 prc-ButtonGroup-ButtonGroup-vcMeG"><div><span role="tooltip" aria-label="Edit this file" id=":R6ksptal9lab:" class="Tooltip__TooltipBase-sc-17tf59c-0 fiSvBN tooltipped-nw"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Edit file" data-testid="edit-button" class="Box-sc-g0xbh4-0 kilKoS prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rmksptal9lab:-loading-announcement" href="https://github.com/Oliver-JC-Li/rag_demo/edit/main/stop360_multiturn_rag_v2.py" data-hotkey="e,Shift+E"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a></span></div><div><button data-component="IconButton" type="button" aria-label="More edit options" data-testid="more-edit-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Raksptal9lab:-loading-announcement" id=":Raksptal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button></div></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><span role="tooltip" aria-label="Open symbols panel" id=":R5sptal9lab:" class="Tooltip__TooltipBase-sc-17tf59c-0 fiSvBN tooltipped-nw"><button data-component="IconButton" type="button" aria-label="Symbols" aria-pressed="false" aria-expanded="false" aria-controls="symbols-pane" data-testid="symbols-button" class="Box-sc-g0xbh4-0 hySUEo prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby="symbols-button-loading-announcement" id="symbols-button" data-hotkey="Meta+i"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button></span><div class="react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" aria-label="Edit and raw actions" title="More file actions" data-testid="more-file-actions-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="Box-sc-g0xbh4-0 itGLhU prc-Button-ButtonBase-c50BI js-blob-dropdown-click prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":Rnsptal9lab:-loading-announcement" id=":Rnsptal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button></div></div></div></div><div><div class="Box-sc-g0xbh4-0 fFkAHo"><div class="Box-sc-g0xbh4-0 kGicmb"><div class="Box-sc-g0xbh4-0 ppLhD react-line-numbers"><div data-line-number="50" class="react-line-number react-code-text" style="padding-right: 16px;">50</div></div><div class="react-code-lines"><div class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div" style="padding-left: 18px;"><span class="pl-s1">system_prompt</span> <span class="pl-c1">=</span> (<span class="pl-s">"""</span></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 hycJXc"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 dceWRL"><div class="Box-sc-g0xbh4-0 dGXHv"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="Box-sc-g0xbh4-0 bpDFns"><div class="Box-sc-g0xbh4-0 iJOeCH"><div class="Box-sc-g0xbh4-0 eJSJhL"><div class="Box-sc-g0xbh4-0 hmoDKB"><div aria-hidden="true" data-testid="navigation-cursor" class="Box-sc-g0xbh4-0 code-navigation-cursor" style="top: 0px; left: 92px;"> </div><button hidden="" data-testid="NavigationCursorEnter" data-hotkey="Meta+Enter" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightedLine" data-hotkey="Shift+J" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightAndExpandMenu" data-hotkey="Alt+Shift+C,Alt+Shift+Ç" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageDown" data-hotkey="PageDown" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageUp" data-hotkey="PageUp" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div><textarea id="read-only-cursor-text-area" data-testid="read-only-cursor-text-area" aria-label="file content" aria-readonly="true" inputmode="none" tabindex="0" aria-multiline="true" aria-haspopup="false" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" spellcheck="false" autocorrect="off" autocapitalize="off" autocomplete="off" data-ms-editor="false" class="react-blob-textarea react-blob-print-hide" style="resize: none; margin-top: -2px; padding-left: 92px; padding-right: 70px; width: 100%; background-color: unset; box-sizing: border-box; color: transparent; position: absolute; border: none; tab-size: 8; outline: none; overflow: auto hidden; height: 2380px; font-size: 12px; line-height: 20px; overflow-wrap: normal; overscroll-behavior-x: none; white-space: pre; z-index: 1;">from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st


openai_api_key = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(model='gpt-4o-mini', api_key=openai_api_key)

# Load the documents
loader = PyPDFLoader("./stop360/STOP360_Template.pdf")
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
doc_chunks = text_splitter.split_documents(docs)
vector_db = FAISS.from_documents(doc_chunks, embedding=OpenAIEmbeddings())
retriever = vector_db.as_retriever()

# Contextualize question
context_q_system_prompt = ("""
Given a chat history and the latest user question which might
reference context in the chat history, formulate a standalone
question which can be understood without the chat history. Do
NOT answer the question, just reformulate it if needed and otherwise
return it as is.
""")

llm = ChatOpenAI(model='gpt-4o-mini')

context_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", context_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]

)
history_aware_retriever = create_history_aware_retriever(llm, retriever, context_q_prompt)

# Question Answering
system_prompt = ("""
You are an assistant for question-answering tasks. Use the following
pieces of retrieved context to answer the question.
&lt;context&gt;
{context}
&lt;/context&gt;
""")

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)


# Manage chat history
chat_history = {}


def get_session_history(session_id: str) -&gt; BaseChatMessageHistory:
    if session_id not in chat_history:
        chat_history[session_id] = ChatMessageHistory()
    return chat_history[session_id]


conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

# Streamlit framework
vector_store = []
st.header("STOP360 conversational chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="I am a vertual study assistant, please as any question regarding STOP360 study")
    ]

if vector_store not in st.session_state:
    st.session_state.vector_store = retriever

user_input = st.chat_input("Ask you question over here")

if user_input is not None and user_input.strip() != "":
    response = conversational_rag_chain.invoke(
        {'input': user_input},
        config={
            "configurable": {"session_id": "stop360_1"}
        }
    )['answer']

    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.chat_history.append(AIMessage(content=response))

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    else:
        with st.chat_message("Human"):
            st.write(message.content)</textarea><button hidden="" data-testid="" data-hotkey="Alt+F1,Control+Alt+˙,Control+Alt+h" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 kHHiZS"><div tabindex="0" class="Box-sc-g0xbh4-0 jqUoVd"><div class="Box-sc-g0xbh4-0 jTRPUP react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="8" data-paste-markdown-skip="true" data-hpc="true"><div class="react-line-numbers-no-virtualization" style="pointer-events: auto; position: relative; z-index: 2;"><div class="react-no-virtualization-wrapper-lines"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right: 16px;">1</div><div data-line-number="2" class="react-line-number react-code-text" style="padding-right: 16px;">2</div><div data-line-number="3" class="react-line-number react-code-text" style="padding-right: 16px;">3</div><div data-line-number="4" class="react-line-number react-code-text" style="padding-right: 16px;">4</div><div data-line-number="5" class="react-line-number react-code-text" style="padding-right: 16px;">5</div><div data-line-number="6" class="react-line-number react-code-text" style="padding-right: 16px;">6</div><div data-line-number="7" class="react-line-number react-code-text" style="padding-right: 16px;">7</div><div data-line-number="8" class="react-line-number react-code-text" style="padding-right: 16px;">8</div><div data-line-number="9" class="react-line-number react-code-text" style="padding-right: 16px;">9</div><div data-line-number="10" class="react-line-number react-code-text" style="padding-right: 16px;">10</div><div data-line-number="11" class="react-line-number react-code-text" style="padding-right: 16px;">11</div><div data-line-number="12" class="react-line-number react-code-text" style="padding-right: 16px;">12</div><div data-line-number="13" class="react-line-number react-code-text" style="padding-right: 16px;">13</div><div data-line-number="14" class="react-line-number react-code-text" style="padding-right: 16px;">14</div><div data-line-number="15" class="react-line-number react-code-text" style="padding-right: 16px;">15</div><div data-line-number="16" class="react-line-number react-code-text" style="padding-right: 16px;">16</div><div data-line-number="17" class="react-line-number react-code-text" style="padding-right: 16px;">17</div><div data-line-number="18" class="react-line-number react-code-text" style="padding-right: 16px;">18</div><div data-line-number="19" class="react-line-number react-code-text" style="padding-right: 16px;">19</div><div data-line-number="20" class="react-line-number react-code-text" style="padding-right: 16px;">20</div><div data-line-number="21" class="react-line-number react-code-text" style="padding-right: 16px;">21</div><div data-line-number="22" class="react-line-number react-code-text" style="padding-right: 16px;">22</div><div data-line-number="23" class="react-line-number react-code-text" style="padding-right: 16px;">23</div><div data-line-number="24" class="react-line-number react-code-text" style="padding-right: 16px;">24</div><div data-line-number="25" class="react-line-number react-code-text" style="padding-right: 16px;">25</div><div data-line-number="26" class="react-line-number react-code-text" style="padding-right: 16px;">26</div><div data-line-number="27" class="react-line-number react-code-text" style="padding-right: 16px;">27</div><div data-line-number="28" class="react-line-number react-code-text" style="padding-right: 16px;">28</div><div data-line-number="29" class="react-line-number react-code-text" style="padding-right: 16px;">29<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="30" class="child-of-line-28  react-line-number react-code-text" style="padding-right: 16px;">30</div><div data-line-number="31" class="child-of-line-28  react-line-number react-code-text" style="padding-right: 16px;">31</div><div data-line-number="32" class="child-of-line-28  react-line-number react-code-text" style="padding-right: 16px;">32</div><div data-line-number="33" class="child-of-line-28  react-line-number react-code-text" style="padding-right: 16px;">33</div><div data-line-number="34" class="child-of-line-28  react-line-number react-code-text" style="padding-right: 16px;">34</div><div data-line-number="35" class="react-line-number react-code-text" style="padding-right: 16px;">35</div><div data-line-number="36" class="react-line-number react-code-text" style="padding-right: 16px;">36</div><div data-line-number="37" class="react-line-number react-code-text" style="padding-right: 16px;">37</div><div data-line-number="38" class="react-line-number react-code-text" style="padding-right: 16px;">38</div><div data-line-number="39" class="react-line-number react-code-text" style="padding-right: 16px;">39<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="40" class="child-of-line-38  react-line-number react-code-text" style="padding-right: 16px;">40</div><div data-line-number="41" class="child-of-line-38  react-line-number react-code-text" style="padding-right: 16px;">41</div><div data-line-number="42" class="child-of-line-38  react-line-number react-code-text" style="padding-right: 16px;">42</div><div data-line-number="43" class="child-of-line-38  react-line-number react-code-text" style="padding-right: 16px;">43</div><div data-line-number="44" class="child-of-line-38  react-line-number react-code-text" style="padding-right: 16px;">44</div><div data-line-number="45" class="child-of-line-38  react-line-number react-code-text" style="padding-right: 16px;">45</div><div data-line-number="46" class="react-line-number react-code-text" style="padding-right: 16px;">46</div><div data-line-number="47" class="react-line-number react-code-text" style="padding-right: 16px;">47</div><div data-line-number="48" class="react-line-number react-code-text" style="padding-right: 16px;">48</div><div data-line-number="49" class="react-line-number react-code-text" style="padding-right: 16px;">49</div><div data-line-number="50" class="react-line-number react-code-text" style="padding-right: 16px;">50<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="51" class="child-of-line-49  react-line-number react-code-text" style="padding-right: 16px;">51</div><div data-line-number="52" class="child-of-line-49  react-line-number react-code-text" style="padding-right: 16px;">52</div><div data-line-number="53" class="child-of-line-49  react-line-number react-code-text" style="padding-right: 16px;">53</div><div data-line-number="54" class="child-of-line-49  react-line-number react-code-text" style="padding-right: 16px;">54</div><div data-line-number="55" class="child-of-line-49  react-line-number react-code-text" style="padding-right: 16px;">55</div><div data-line-number="56" class="react-line-number react-code-text" style="padding-right: 16px;">56</div><div data-line-number="57" class="react-line-number react-code-text" style="padding-right: 16px;">57</div><div data-line-number="58" class="react-line-number react-code-text" style="padding-right: 16px;">58<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="59" class="child-of-line-57  react-line-number react-code-text" style="padding-right: 16px;">59</div><div data-line-number="60" class="child-of-line-57  react-line-number react-code-text" style="padding-right: 16px;">60</div></div><div class="react-no-virtualization-wrapper-lines"><div data-line-number="61" class="child-of-line-57  react-line-number react-code-text" style="padding-right: 16px;">61</div><div data-line-number="62" class="child-of-line-57  react-line-number react-code-text" style="padding-right: 16px;">62</div><div data-line-number="63" class="child-of-line-57  react-line-number react-code-text" style="padding-right: 16px;">63</div><div data-line-number="64" class="react-line-number react-code-text" style="padding-right: 16px;">64</div><div data-line-number="65" class="react-line-number react-code-text" style="padding-right: 16px;">65</div><div data-line-number="66" class="react-line-number react-code-text" style="padding-right: 16px;">66</div><div data-line-number="67" class="react-line-number react-code-text" style="padding-right: 16px;">67</div><div data-line-number="68" class="react-line-number react-code-text" style="padding-right: 16px;">68</div><div data-line-number="69" class="react-line-number react-code-text" style="padding-right: 16px;">69</div><div data-line-number="70" class="react-line-number react-code-text" style="padding-right: 16px;">70</div><div data-line-number="71" class="react-line-number react-code-text" style="padding-right: 16px;">71</div><div data-line-number="72" class="react-line-number react-code-text" style="padding-right: 16px;">72</div><div data-line-number="73" class="react-line-number react-code-text" style="padding-right: 16px;">73</div><div data-line-number="74" class="react-line-number react-code-text" style="padding-right: 16px;">74</div><div data-line-number="75" class="react-line-number react-code-text" style="padding-right: 16px;">75</div><div data-line-number="76" class="react-line-number react-code-text" style="padding-right: 16px;">76</div><div data-line-number="77" class="react-line-number react-code-text" style="padding-right: 16px;">77</div><div data-line-number="78" class="react-line-number react-code-text" style="padding-right: 16px;">78</div><div data-line-number="79" class="react-line-number react-code-text" style="padding-right: 16px;">79<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="80" class="child-of-line-78  react-line-number react-code-text" style="padding-right: 16px;">80</div><div data-line-number="81" class="child-of-line-78  react-line-number react-code-text" style="padding-right: 16px;">81</div><div data-line-number="82" class="child-of-line-78  react-line-number react-code-text" style="padding-right: 16px;">82</div><div data-line-number="83" class="child-of-line-78  react-line-number react-code-text" style="padding-right: 16px;">83</div><div data-line-number="84" class="child-of-line-78  react-line-number react-code-text" style="padding-right: 16px;">84</div><div data-line-number="85" class="react-line-number react-code-text" style="padding-right: 16px;">85</div><div data-line-number="86" class="react-line-number react-code-text" style="padding-right: 16px;">86</div><div data-line-number="87" class="react-line-number react-code-text" style="padding-right: 16px;">87</div><div data-line-number="88" class="react-line-number react-code-text" style="padding-right: 16px;">88</div><div data-line-number="89" class="react-line-number react-code-text" style="padding-right: 16px;">89</div><div data-line-number="90" class="react-line-number react-code-text" style="padding-right: 16px;">90</div><div data-line-number="91" class="react-line-number react-code-text" style="padding-right: 16px;">91</div><div data-line-number="92" class="react-line-number react-code-text" style="padding-right: 16px;">92</div><div data-line-number="93" class="react-line-number react-code-text" style="padding-right: 16px;">93</div><div data-line-number="94" class="react-line-number react-code-text" style="padding-right: 16px;">94</div><div data-line-number="95" class="react-line-number react-code-text" style="padding-right: 16px;">95</div><div data-line-number="96" class="react-line-number react-code-text" style="padding-right: 16px;">96</div><div data-line-number="97" class="react-line-number react-code-text" style="padding-right: 16px;">97</div><div data-line-number="98" class="react-line-number react-code-text" style="padding-right: 16px;">98</div><div data-line-number="99" class="react-line-number react-code-text" style="padding-right: 16px;">99</div><div data-line-number="100" class="react-line-number react-code-text" style="padding-right: 16px;">100</div><div data-line-number="101" class="react-line-number react-code-text" style="padding-right: 16px;">101</div><div data-line-number="102" class="react-line-number react-code-text" style="padding-right: 16px;">102</div><div data-line-number="103" class="react-line-number react-code-text" style="padding-right: 16px;">103</div><div data-line-number="104" class="react-line-number react-code-text" style="padding-right: 16px;">104</div><div data-line-number="105" class="react-line-number react-code-text" style="padding-right: 16px;">105</div><div data-line-number="106" class="react-line-number react-code-text" style="padding-right: 16px;">106</div><div data-line-number="107" class="react-line-number react-code-text" style="padding-right: 16px;">107</div><div data-line-number="108" class="react-line-number react-code-text" style="padding-right: 16px;">108</div><div data-line-number="109" class="react-line-number react-code-text" style="padding-right: 16px;">109</div><div data-line-number="110" class="react-line-number react-code-text" style="padding-right: 16px;">110</div><div data-line-number="111" class="react-line-number react-code-text" style="padding-right: 16px;">111</div><div data-line-number="112" class="react-line-number react-code-text" style="padding-right: 16px;">112</div><div data-line-number="113" class="react-line-number react-code-text" style="padding-right: 16px;">113</div><div data-line-number="114" class="react-line-number react-code-text" style="padding-right: 16px;">114</div><div data-line-number="115" class="react-line-number react-code-text" style="padding-right: 16px;">115</div><div data-line-number="116" class="react-line-number react-code-text" style="padding-right: 16px;">116</div><div data-line-number="117" class="react-line-number react-code-text" style="padding-right: 16px;">117</div><div data-line-number="118" class="react-line-number react-code-text" style="padding-right: 16px;">118</div></div></div><div class="react-code-lines"><div inert="inert"><div class="react-no-virtualization-wrapper"><div id="LC1" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain_community</span>.<span class="pl-s1">document_loaders</span> <span class="pl-k">import</span> <span class="pl-v">PyPDFLoader</span></div>
<div id="LC2" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain</span>.<span class="pl-s1">text_splitter</span> <span class="pl-k">import</span> <span class="pl-v">RecursiveCharacterTextSplitter</span></div>
<div id="LC3" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain_community</span>.<span class="pl-s1">vectorstores</span> <span class="pl-k">import</span> <span class="pl-c1">FAISS</span></div>
<div id="LC4" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain_openai</span> <span class="pl-k">import</span> <span class="pl-v">ChatOpenAI</span>, <span class="pl-v">OpenAIEmbeddings</span></div>
<div id="LC5" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain</span>.<span class="pl-s1">prompts</span> <span class="pl-k">import</span> <span class="pl-v">ChatPromptTemplate</span>, <span class="pl-v">MessagesPlaceholder</span></div>
<div id="LC6" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain</span>.<span class="pl-s1">chains</span>.<span class="pl-s1">combine_documents</span> <span class="pl-k">import</span> <span class="pl-s1">create_stuff_documents_chain</span></div>
<div id="LC7" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain</span>.<span class="pl-s1">chains</span>.<span class="pl-s1">history_aware_retriever</span> <span class="pl-k">import</span> <span class="pl-s1">create_history_aware_retriever</span></div>
<div id="LC8" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain</span>.<span class="pl-s1">chains</span>.<span class="pl-s1">retrieval</span> <span class="pl-k">import</span> <span class="pl-s1">create_retrieval_chain</span></div>
<div id="LC9" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain_community</span>.<span class="pl-s1">chat_message_histories</span> <span class="pl-k">import</span> <span class="pl-v">ChatMessageHistory</span></div>
<div id="LC10" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain_core</span>.<span class="pl-s1">chat_history</span> <span class="pl-k">import</span> <span class="pl-v">BaseChatMessageHistory</span></div>
<div id="LC11" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain_core</span>.<span class="pl-s1">runnables</span>.<span class="pl-s1">history</span> <span class="pl-k">import</span> <span class="pl-v">RunnableWithMessageHistory</span></div>
<div id="LC12" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">from</span> <span class="pl-s1">langchain_core</span>.<span class="pl-s1">messages</span> <span class="pl-k">import</span> <span class="pl-v">HumanMessage</span>, <span class="pl-v">AIMessage</span></div>
<div id="LC13" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">import</span> <span class="pl-s1">streamlit</span> <span class="pl-k">as</span> <span class="pl-s1">st</span></div>
<div id="LC14" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC15" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC16" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">openai_api_key</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">secrets</span>[<span class="pl-s">"OPENAI_API_KEY"</span>]</div>
<div id="LC17" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC18" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">llm</span> <span class="pl-c1">=</span> <span class="pl-en">ChatOpenAI</span>(<span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">'gpt-4o-mini'</span>, <span class="pl-s1">api_key</span><span class="pl-c1">=</span><span class="pl-s1">openai_api_key</span>)</div>
<div id="LC19" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC20" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Load the documents</span></div>
<div id="LC21" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">loader</span> <span class="pl-c1">=</span> <span class="pl-en">PyPDFLoader</span>(<span class="pl-s">"./stop360/STOP360_Template.pdf"</span>)</div>
<div id="LC22" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">docs</span> <span class="pl-c1">=</span> <span class="pl-s1">loader</span>.<span class="pl-c1">load</span>()</div>
<div id="LC23" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">text_splitter</span> <span class="pl-c1">=</span> <span class="pl-en">RecursiveCharacterTextSplitter</span>(<span class="pl-s1">chunk_size</span><span class="pl-c1">=</span><span class="pl-c1">1000</span>, <span class="pl-s1">chunk_overlap</span><span class="pl-c1">=</span><span class="pl-c1">20</span>)</div>
<div id="LC24" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">doc_chunks</span> <span class="pl-c1">=</span> <span class="pl-s1">text_splitter</span>.<span class="pl-c1">split_documents</span>(<span class="pl-s1">docs</span>)</div>
<div id="LC25" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">vector_db</span> <span class="pl-c1">=</span> <span class="pl-c1">FAISS</span>.<span class="pl-c1">from_documents</span>(<span class="pl-s1">doc_chunks</span>, <span class="pl-s1">embedding</span><span class="pl-c1">=</span><span class="pl-en">OpenAIEmbeddings</span>())</div>
<div id="LC26" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">retriever</span> <span class="pl-c1">=</span> <span class="pl-s1">vector_db</span>.<span class="pl-c1">as_retriever</span>()</div>
<div id="LC27" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC28" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Contextualize question</span></div>
<div id="LC29" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">context_q_system_prompt</span> <span class="pl-c1">=</span> (<span class="pl-s">"""</span></div>
<div id="LC30" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-28 "><span class="pl-s">Given a chat history and the latest user question which might</span></div>
<div id="LC31" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-28 "><span class="pl-s">reference context in the chat history, formulate a standalone</span></div>
<div id="LC32" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-28 "><span class="pl-s">question which can be understood without the chat history. Do</span></div>
<div id="LC33" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-28 "><span class="pl-s">NOT answer the question, just reformulate it if needed and otherwise</span></div>
<div id="LC34" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-28 "><span class="pl-s">return it as is.</span></div>
<div id="LC35" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s">"""</span>)</div>
<div id="LC36" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC37" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">llm</span> <span class="pl-c1">=</span> <span class="pl-en">ChatOpenAI</span>(<span class="pl-s1">model</span><span class="pl-c1">=</span><span class="pl-s">'gpt-4o-mini'</span>)</div>
<div id="LC38" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC39" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">context_q_prompt</span> <span class="pl-c1">=</span> <span class="pl-v">ChatPromptTemplate</span>.<span class="pl-c1">from_messages</span>(</div>
<div id="LC40" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-38 ">    [</div>
<div id="LC41" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-38 ">        (<span class="pl-s">"system"</span>, <span class="pl-s1">context_q_system_prompt</span>),</div>
<div id="LC42" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-38 ">        <span class="pl-en">MessagesPlaceholder</span>(<span class="pl-s">"chat_history"</span>),</div>
<div id="LC43" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-38 ">        (<span class="pl-s">"human"</span>, <span class="pl-s">"{input}"</span>)</div>
<div id="LC44" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-38 ">    ]</div>
<div id="LC45" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-38 ">
</div>
<div id="LC46" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">)</div>
<div id="LC47" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">history_aware_retriever</span> <span class="pl-c1">=</span> <span class="pl-en">create_history_aware_retriever</span>(<span class="pl-s1">llm</span>, <span class="pl-s1">retriever</span>, <span class="pl-s1">context_q_prompt</span>)</div>
<div id="LC48" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC49" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Question Answering</span></div>
<div id="LC50" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">system_prompt</span> <span class="pl-c1">=</span> (<span class="pl-s">"""</span></div>
<div id="LC51" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-49 "><span class="pl-s">You are an assistant for question-answering tasks. Use the following</span></div>
<div id="LC52" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-49 "><span class="pl-s">pieces of retrieved context to answer the question.</span></div>
<div id="LC53" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-49 "><span class="pl-s">&lt;context&gt;</span></div>
<div id="LC54" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-49 "><span class="pl-s">{context}</span></div>
<div id="LC55" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-49 "><span class="pl-s">&lt;/context&gt;</span></div>
<div id="LC56" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s">"""</span>)</div>
<div id="LC57" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC58" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">qa_prompt</span> <span class="pl-c1">=</span> <span class="pl-v">ChatPromptTemplate</span>.<span class="pl-c1">from_messages</span>(</div>
<div id="LC59" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-57 ">    [</div>
<div id="LC60" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-57 ">        (<span class="pl-s">"system"</span>, <span class="pl-s1">system_prompt</span>),</div></div>
<div class="react-no-virtualization-wrapper"><div id="LC61" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-57 ">        <span class="pl-en">MessagesPlaceholder</span>(<span class="pl-s">"chat_history"</span>),</div>
<div id="LC62" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-57 ">        (<span class="pl-s">"human"</span>, <span class="pl-s">"{input}"</span>)</div>
<div id="LC63" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-57 ">    ]</div>
<div id="LC64" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">)</div>
<div id="LC65" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">question_answer_chain</span> <span class="pl-c1">=</span> <span class="pl-en">create_stuff_documents_chain</span>(<span class="pl-s1">llm</span>, <span class="pl-s1">qa_prompt</span>)</div>
<div id="LC66" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">rag_chain</span> <span class="pl-c1">=</span> <span class="pl-en">create_retrieval_chain</span>(<span class="pl-s1">history_aware_retriever</span>, <span class="pl-s1">question_answer_chain</span>)</div>
<div id="LC67" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC68" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC69" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Manage chat history</span></div>
<div id="LC70" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">chat_history</span> <span class="pl-c1">=</span> {}</div>
<div id="LC71" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC72" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC73" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">def</span> <span class="pl-en">get_session_history</span>(<span class="pl-s1">session_id</span>: <span class="pl-smi">str</span>) <span class="pl-c1">-&gt;</span> <span class="pl-smi">BaseChatMessageHistory</span>:</div>
<div id="LC74" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">if</span> <span class="pl-s1">session_id</span> <span class="pl-c1"><span class="pl-c1">not</span> <span class="pl-c1">in</span></span> <span class="pl-s1">chat_history</span>:</div>
<div id="LC75" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-s1">chat_history</span>[<span class="pl-s1">session_id</span>] <span class="pl-c1">=</span> <span class="pl-en">ChatMessageHistory</span>()</div>
<div id="LC76" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">return</span> <span class="pl-s1">chat_history</span>[<span class="pl-s1">session_id</span>]</div>
<div id="LC77" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC78" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC79" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">conversational_rag_chain</span> <span class="pl-c1">=</span> <span class="pl-en">RunnableWithMessageHistory</span>(</div>
<div id="LC80" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-78 ">    <span class="pl-s1">rag_chain</span>,</div>
<div id="LC81" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-78 ">    <span class="pl-s1">get_session_history</span>,</div>
<div id="LC82" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-78 ">    <span class="pl-s1">input_messages_key</span><span class="pl-c1">=</span><span class="pl-s">"input"</span>,</div>
<div id="LC83" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-78 ">    <span class="pl-s1">history_messages_key</span><span class="pl-c1">=</span><span class="pl-s">"chat_history"</span>,</div>
<div id="LC84" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div child-of-line-78 ">    <span class="pl-s1">output_messages_key</span><span class="pl-c1">=</span><span class="pl-s">"answer"</span></div>
<div id="LC85" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">)</div>
<div id="LC86" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC87" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"># Streamlit framework</span></div>
<div id="LC88" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">vector_store</span> <span class="pl-c1">=</span> []</div>
<div id="LC89" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">st</span>.<span class="pl-c1">header</span>(<span class="pl-s">"STOP360 conversational chatbot"</span>)</div>
<div id="LC90" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC91" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">if</span> <span class="pl-s">"chat_history"</span> <span class="pl-c1"><span class="pl-c1">not</span> <span class="pl-c1">in</span></span> <span class="pl-s1">st</span>.<span class="pl-c1">session_state</span>:</div>
<div id="LC92" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">st</span>.<span class="pl-c1">session_state</span>.<span class="pl-c1">chat_history</span> <span class="pl-c1">=</span> [</div>
<div id="LC93" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-en">AIMessage</span>(<span class="pl-s1">content</span><span class="pl-c1">=</span><span class="pl-s">"I am a vertual study assistant, please as any question regarding STOP360 study"</span>)</div>
<div id="LC94" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    ]</div>
<div id="LC95" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC96" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">if</span> <span class="pl-s1">vector_store</span> <span class="pl-c1"><span class="pl-c1">not</span> <span class="pl-c1">in</span></span> <span class="pl-s1">st</span>.<span class="pl-c1">session_state</span>:</div>
<div id="LC97" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">st</span>.<span class="pl-c1">session_state</span>.<span class="pl-c1">vector_store</span> <span class="pl-c1">=</span> <span class="pl-s1">retriever</span></div>
<div id="LC98" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC99" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">user_input</span> <span class="pl-c1">=</span> <span class="pl-s1">st</span>.<span class="pl-c1">chat_input</span>(<span class="pl-s">"Ask you question over here"</span>)</div>
<div id="LC100" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC101" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">if</span> <span class="pl-s1">user_input</span> <span class="pl-c1"><span class="pl-c1">is</span> <span class="pl-c1">not</span></span> <span class="pl-c1">None</span> <span class="pl-c1">and</span> <span class="pl-s1">user_input</span>.<span class="pl-c1">strip</span>() <span class="pl-c1">!=</span> <span class="pl-s">""</span>:</div>
<div id="LC102" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">response</span> <span class="pl-c1">=</span> <span class="pl-s1">conversational_rag_chain</span>.<span class="pl-c1">invoke</span>(</div>
<div id="LC103" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        {<span class="pl-s">'input'</span>: <span class="pl-s1">user_input</span>},</div>
<div id="LC104" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-s1">config</span><span class="pl-c1">=</span>{</div>
<div id="LC105" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-s">"configurable"</span>: {<span class="pl-s">"session_id"</span>: <span class="pl-s">"stop360_1"</span>}</div>
<div id="LC106" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        }</div>
<div id="LC107" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    )[<span class="pl-s">'answer'</span>]</div>
<div id="LC108" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC109" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">st</span>.<span class="pl-c1">session_state</span>.<span class="pl-c1">chat_history</span>.<span class="pl-c1">append</span>(<span class="pl-en">HumanMessage</span>(<span class="pl-s1">content</span><span class="pl-c1">=</span><span class="pl-s1">user_input</span>))</div>
<div id="LC110" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s1">st</span>.<span class="pl-c1">session_state</span>.<span class="pl-c1">chat_history</span>.<span class="pl-c1">append</span>(<span class="pl-en">AIMessage</span>(<span class="pl-s1">content</span><span class="pl-c1">=</span><span class="pl-s1">response</span>))</div>
<div id="LC111" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC112" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">for</span> <span class="pl-s1">message</span> <span class="pl-c1">in</span> <span class="pl-s1">st</span>.<span class="pl-c1">session_state</span>.<span class="pl-c1">chat_history</span>:</div>
<div id="LC113" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">if</span> <span class="pl-en">isinstance</span>(<span class="pl-s1">message</span>, <span class="pl-v">AIMessage</span>):</div>
<div id="LC114" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">with</span> <span class="pl-s1">st</span>.<span class="pl-c1">chat_message</span>(<span class="pl-s">"AI"</span>):</div>
<div id="LC115" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-s1">st</span>.<span class="pl-c1">write</span>(<span class="pl-s1">message</span>.<span class="pl-c1">content</span>)</div>
<div id="LC116" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">else</span>:</div>
<div id="LC117" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">with</span> <span class="pl-s1">st</span>.<span class="pl-c1">chat_message</span>(<span class="pl-s">"Human"</span>):</div>
<div id="LC118" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-s1">st</span>.<span class="pl-c1">write</span>(<span class="pl-s1">message</span>.<span class="pl-c1">content</span>)</div></div></div><div class="Box-sc-g0xbh4-0 gQuAAB symbol-highlight react-code-text" data-testid="sticky-line-observer"></div><div class="Box-sc-g0xbh4-0 jvkXhf symbol-highlight react-code-text" data-testid="sticky-line-observer"></div><div class="Box-sc-g0xbh4-0 sBWBr symbol-highlight react-code-text" data-testid="sticky-line-observer"></div><div class="Box-sc-g0xbh4-0 kyVEQO symbol-highlight react-code-text" data-testid="sticky-line-observer"></div><div class="Box-sc-g0xbh4-0 gfgdLE symbol-highlight react-code-text" data-testid="sticky-line-observer"></div></div><button hidden="" data-hotkey="Meta+a"></button></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div></section></div></div></div> <!-- --> <!-- --> </div></div></div><div class="Box-sc-g0xbh4-0"></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 cCoXib"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Meta+F6,Meta+Shift+F6"></button><button hidden="" data-hotkey="Meta+F6,Meta+Shift+F6"></button></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"night"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.9225 1 1 5.9225 1 12C1 16.8675 4.14875 20.9787 8.52125 22.4362C9.07125 22.5325 9.2775 22.2025 9.2775 21.9137C9.2775 21.6525 9.26375 20.7862 9.26375 19.865C6.5 20.3737 5.785 19.1912 5.565 18.5725C5.44125 18.2562 4.905 17.28 4.4375 17.0187C4.0525 16.8125 3.5025 16.3037 4.42375 16.29C5.29 16.2762 5.90875 17.0875 6.115 17.4175C7.105 19.0812 8.68625 18.6137 9.31875 18.325C9.415 17.61 9.70375 17.1287 10.02 16.8537C7.5725 16.5787 5.015 15.63 5.015 11.4225C5.015 10.2262 5.44125 9.23625 6.1425 8.46625C6.0325 8.19125 5.6475 7.06375 6.2525 5.55125C6.2525 5.55125 7.17375 5.2625 9.2775 6.67875C10.1575 6.43125 11.0925 6.3075 12.0275 6.3075C12.9625 6.3075 13.8975 6.43125 14.7775 6.67875C16.8813 5.24875 17.8025 5.55125 17.8025 5.55125C18.4075 7.06375 18.0225 8.19125 17.9125 8.46625C18.6138 9.23625 19.04 10.2125 19.04 11.4225C19.04 15.6437 16.4688 16.5787 14.0213 16.8537C14.42 17.1975 14.7638 17.8575 14.7638 18.8887C14.7638 20.36 14.75 21.5425 14.75 21.9137C14.75 22.2025 14.9563 22.5462 15.5063 22.4362C19.8513 20.9787 23 16.8537 23 12C23 5.9225 18.0775 1 12 1Z"></path>
</svg>
</a>
      <span>
        © 2025 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/Oliver-JC-Li"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/Oliver-JC-Li"]:before,
      .user-mention[href$="/Oliver-JC-Li"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true">rag_demo/stop360_multiturn_rag_v2.py at main · Oliver-JC-Li/rag_demo</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive">&nbsp;</div></body><grammarly-desktop-integration data-grammarly-shadow-root="true"><template shadowrootmode="open"><style>
      div.grammarly-desktop-integration {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select:none;
        user-select:none;
      }

      div.grammarly-desktop-integration:before {
        content: attr(data-content);
      }
    </style><div aria-label="grammarly-integration" role="group" tabindex="-1" class="grammarly-desktop-integration" data-content="{&quot;mode&quot;:&quot;full&quot;,&quot;isActive&quot;:true,&quot;isUserDisabled&quot;:false,&quot;isAlwaysAvailableAssistantEnabled&quot;:false}"></div></template></grammarly-desktop-integration></html>