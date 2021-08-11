#抓取資料
import json
#抓取medium.com 文章資料
# import urllib.request as req
# url = "http://link.medium.com/a/key_live_ofxXr2qTrrU9NqURK8ZwEhknBxiI6KBm?%24identity_id=905471419614208381"
# #建立一個Request物件 附加Request Headers的訊息
# request = req.Request(url, headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("UTF-8") #根據觀察 取得是JSON資料
# # print(data)
# #解析 JSON格式資料 取得標題
# import json
# data = json.loads(data) #把原始JSON資諒解析成字典/列表格式
# print(data)

#抓取medium.com 文章資料 加入Reqest Data 概念
import urllib.request as req
#建立連線網址
url = "https://medium.com/_/graphql"
#建立一個Request物件 附加Request Headers 和 Reqest Data 的訊息
requestData ={
    "operationName": "ExtendedFeedQuery",
    "query": "query ExtendedFeedQuery($items: [ExtendedFeedItemOptions!]!) {\n  extendedFeedItems(items: $items) {\n    post {\n      ...PostListModulePostPreviewData\n      __typename\n    }\n    metadata {\n      topic {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PostListModulePostPreviewData on Post {\n  id\n  firstPublishedAt\n  readingTime\n  createdAt\n  mediumUrl\n  previewImage {\n    id\n    __typename\n  }\n  title\n  collection {\n    id\n    domain\n    slug\n    name\n    navItems {\n      url\n      __typename\n    }\n    logo {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    ...userUrl_user\n    __typename\n  }\n  visibility\n  isProxyPost\n  isLocked\n  ...HomeFeedItem_post\n  ...HomeTrendingModule_post\n  __typename\n}\n\nfragment HomeFeedItem_post on Post {\n  __typename\n  id\n  title\n  firstPublishedAt\n  mediumUrl\n  collection {\n    id\n    name\n    domain\n    logo {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  readingTime\n  tags {\n    ...TopicPill_tag\n    __typename\n  }\n  ...BookmarkButton_post\n  ...CreatorActionOverflowPopover_post\n  ...PostPresentationTracker_post\n  ...PostPreviewAvatar_post\n}\n\nfragment TopicPill_tag on Tag {\n  __typename\n  id\n  displayTitle\n}\n\nfragment BookmarkButton_post on Post {\n  visibility\n  ...SusiClickable_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        catalogItemIds\n        __typename\n      }\n      predefinedContainingThis {\n        catalogId\n        predefined\n        catalogItemIds\n        __typename\n      }\n      __typename\n    }\n    ...editCatalogItemsMutation_postViewerEdge\n    ...useAddItemToPredefinedCatalog_postViewerEdge\n    __typename\n    id\n  }\n  ...WithToggleInsideCatalog_post\n  __typename\n}\n\nfragment useAddItemToPredefinedCatalog_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    predefinedContainingThis {\n      catalogId\n      version\n      predefined\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment editCatalogItemsMutation_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    catalogsContainingThis(type: LISTS) {\n      catalogId\n      version\n      catalogItemIds\n      __typename\n    }\n    predefinedContainingThis {\n      catalogId\n      predefined\n      version\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment WithToggleInsideCatalog_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        __typename\n      }\n      predefinedContainingThis {\n        predefined\n        __typename\n      }\n      __typename\n    }\n    __typename\n    id\n  }\n  __typename\n}\n\nfragment CreatorActionOverflowPopover_post on Post {\n  allowResponses\n  id\n  statusForCollection\n  isLocked\n  isPublished\n  clapCount\n  mediumUrl\n  pinnedAt\n  pinnedByCreatorAt\n  curationEligibleAt\n  mediumUrl\n  responseDistribution\n  visibility\n  ...useIsPinnedInContext_post\n  pendingCollection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    __typename\n  }\n  creator {\n    id\n    ...MutePopoverOptions_creator\n    ...auroraHooks_publisher\n    __typename\n  }\n  collection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    ...MutePopoverOptions_collection\n    ...auroraHooks_publisher\n    __typename\n  }\n  ...ClapMutation_post\n  __typename\n}\n\nfragment MutePopoverOptions_creator on User {\n  id\n  __typename\n}\n\nfragment MutePopoverOptions_collection on Collection {\n  id\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  ...PostVotersNetwork_post\n  __typename\n}\n\nfragment PostVotersNetwork_post on Post {\n  id\n  voterCount\n  recommenders {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment useIsPinnedInContext_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  pendingCollection {\n    id\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  __typename\n}\n\nfragment auroraHooks_publisher on Publisher {\n  __typename\n  ... on Collection {\n    isAuroraEligible\n    isAuroraVisible\n    viewerEdge {\n      id\n      isEditor\n      __typename\n    }\n    __typename\n    id\n  }\n  ... on User {\n    isAuroraVisible\n    __typename\n    id\n  }\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    ...collectionUrl_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  id\n  imageId\n  mediumMemberAt\n  name\n  username\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  hasSubdomain\n  username\n}\n\nfragment HomeTrendingModule_post on Post {\n  id\n  ...HomeTrendingPostPreview_post\n  __typename\n}\n\nfragment HomeTrendingPostPreview_post on Post {\n  id\n  title\n  mediumUrl\n  readingTime\n  firstPublishedAt\n  ...PostPreviewAvatar_post\n  ...PostPresentationTracker_post\n  __typename\n}\n",
    "variables": {
        "items": [
            {"postId": "fe16da98bb30", "topicId": ""},
            {"postId": "8d4f473b04b", "topicId": ""}, 
            {"postId": "a9f5f87f3118", "topicId": ""},
            {"postId": "d7d825cb9cea", "topicId": ""},
            {"postId": "71c07d0ca1d2","topicId": ""},
            {"postId": "3bce8786f6b4", "topicId": ""},
            {"postId": "1d8b6afcb609", "topicId": ""},
            {"postId": "efc724cfac9e", "topicId": ""},
            {"postId": "755a02673aa9", "topicId": ""},
            {"postId": "469b9c4737c7", "topicId": ""},
            {"postId": "67bf07f011a6", "topicId": ""},
            {"postId": "4de33f4d192c", "topicId": ""},
            {"postId": "cc6c2d3c6775", "topicId": ""},
            {"postId": "f0d35e60f44d", "topicId": ""},
            {"postId": "9a8fc40d823c", "topicId": ""},
            {"postId": "c3239b59474", "topicId": ""},
            {"postId": "f522aac3b97c", "topicId": ""},
            {"postId": "993829a63867", "topicId": ""},
            {"postId": "eac00f7ff510", "topicId": ""},
            {"postId": "8a618a15eca6", "topicId": ""}
        ]
    }
}
request = req.Request(url,headers = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
},data = json.dumps(requestData).encode("utf-8"))

#發出請求
with req.urlopen(request) as response:
    result = response.read().decode("utf-8")
 #解析 JSON格式資料 取得標題
result = json.loads(result)
#print(result["data"]["extendedFeedItems"][0]["post"]["title"])
items = result["data"]["extendedFeedItems"]
for item in items:
    print(item["post"]["title"])