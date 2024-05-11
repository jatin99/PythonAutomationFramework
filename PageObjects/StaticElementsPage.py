from selenium.webdriver.common.by import By


class StaticElements:
    profile = (By.ID,"UProfile")
    tenantDropdown = (By.XPATH,"//span[@class='k-input-value-text']")
    DownloadButton = (By.XPATH, "//span[contains(text(),'Download')]")
    FilterButton = (By.XPATH, "//button[contains(text(),'Filters')]")
    LayoutButton = (By.XPATH, "//button[contains(text(),'Layout')]")
    FavoriteButton = (By.XPATH, "//div[@class='favMenu']/a[1]")
    ShareButton = (By.XPATH, "//div[@class='favMenu']/a[2]")
    Favorite_Name = (By.XPATH, "//div[@class='name-field']/span")
    Favorite_Description = (By.XPATH, "//div[@class='description-field']")
    Favorite_Save = (By.XPATH, "//button[contains(text(),'Save')]")
    Favorite_Cancel = (By.XPATH, "//button[contains(text(),'Cancel')]")
    Share_Name = (By.XPATH, "//div[@class='name-field']/input")
    Share_Description = (By.XPATH, "//div[@class='description-field']/textarea")
    Share_Save = (By.XPATH, "//button[contains(text(),'Save')]")
    Share_Cancel = (By.XPATH, "//button[contains(text(),'Cancel')]")
    SaveButton = (By.NAME, "SaveTransaction")
    DiscardButton = (By.NAME, "DiscardTransaction")
    filter_icon1 = (By.XPATH, "//ul[@data-role='tooltip']/li[1]")
    filter_icon2 = (By.XPATH, "//ul[@data-role='tooltip']/li[2]")
    filter_icon3 = (By.XPATH, "//ul[@data-role='tooltip']/li[3]")
    filter_icon4 = (By.XPATH, "//ul[@data-role='tooltip']/li[4]")
    popupSubmit = (By.XPATH,"//button[@class='k-button k-button-icontext o9-form-button submit-button o9-tabbable']")
    popupclose = (By.XPATH, "//div[@class='button-wrapper']//*[contains(text(),'Close')]")
    bellicon = (By.XPATH,"//i[@class='fa fa-bell']")
    dataverify = (By.XPATH, "// div[@class ='ui-widget-content slick-row even active']")
    expand = (By.XPATH,"//div[@class='page-nav-container view-nav-header']")
    save = (By.XPATH, "//span[normalize-space()='Save']")
    threedots = (By.XPATH,"//div[@id='viewFavourites']/div/span[3]/i")
    designerSettings = (By.XPATH,"//span[contains(text(),'Designer Setting')]")
    designerlayout = (By.ID,"designLayout")
    close = (By.XPATH,"//button[@class='k-button k-button-icontext k-grid-close o9-form-button o9-tabbable']")
    filter1 = (By.XPATH,"//div[@class='o9-content-wrapper']/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[2]/span[1]")
    filterelement1row1 = (By.XPATH,"//div[@class='o9-content-wrapper']/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/span[1]")
    allDept = (By.XPATH, "//span[normalize-space()='All : Department']")
    allgrp  = (By.XPATH,"//span[normalize-space()='All : Group']")
    alldivison = (By.XPATH,"//span[normalize-space()='All : Division']")
    allItemCode = (By.XPATH,"//span[normalize-space()='All : Item Code']")
    itemdept = (By.XPATH, "//span[normalize-space()='All : To Item Department']")
    titledept = (By.XPATH, "//span[normalize-space()='2 - MN SOFT ACCESSORIES']")
    selectalldept = (By.XPATH, "//span[@class='selectAll selectAllButton o9-selected']")
    selectallPeriod = (By.XPATH,"//div[@id='inlineFiltersContainer']//div[10]//span[@class='selectAll selectAllButton o9-selected']")
    MNbottomWear = (By.XPATH, "//h4[normalize-space()='12 - MN BOTTOMS']")
    kidsHome = (By.XPATH,"//h4[normalize-space()='16 - KIDS HOME']")
    MNSoftAccessory = (By.XPATH, "//span[contains(text(),'2 - MN SOFT ACCESSORIES')]")
    apply = (By.ID, "apply")
    cumulative = (By.XPATH,"//input[@class='cumulative-checkbox']")
    filterAllLocation = (By.XPATH, "//span[normalize-space()='All : All Locations']")
    designLayout = (By.XPATH,"//i[@class='fa fa-edit']")
    viewReport = (By.XPATH,"//span[@class='k-link']//span[contains(text(),'Order Review  DCtoStore')]/following-sibling::span")
    editInDesigner = (By.XPATH,"//li[@title='Edit-Order Review  DCtoStore']//span/span/i")

    filterAllYear = (By.XPATH,"//div[@id='viewFilters']//div[3]//span[@class='filter-fTitle'][normalize-space()='CurrentWorkingView']")
    weekFilter = (By.XPATH,"//div[@class='levelHierarchyContainer']//div[@title='Period']/following-sibling::div/span[@data-o9-memberindex='0']")
    selectAllWeek = (By.XPATH,"//span[@class='selectAll selectAllButton o9-selected']")
    expandFilter = (By.XPATH,"//div[@id='dropTargetForFilter']//i[@class='o9con o9con-ellipsis-h']")
    closeReportedMenu = (By.XPATH,"//button[@title='Close'][@id='closeReportMenu']")
    ok = (By.XPATH,"//button[contains(@type,'button')][normalize-space()='OK']")
    ###File UPload####
    fileImport = (By.XPATH, "//a[@id='FileImport']")
    selectFile = (By.XPATH, "//span[contains(text(),'Select files...')]/..")
    selectWhole = (By.XPATH, "//div[@id='LSFileUpload']//input[@name='o9ExportFileUploadElement']")
    upload = (By.XPATH, "//button[@name='o9FileUploadButton']")
    popupOk = (By.XPATH, "//div[@class='k-widget k-window k-dialog']//button[contains(text(),'OK')]")
    closeupload = (By.XPATH,"//div[@class='k-window-titlebar k-hstack']//span[@id='excelimport_wnd_title']/following-sibling::div/a")
    #refresh = (By.XPATH,"//i[@class='fa fa-refresh']")
    refresh = (By.ID,"HeaderRefresh")
    notification = (By.XPATH,"//a[@id='Notification']")
    saveLayout = (By.XPATH,"//button[normalize-space()='Save']")
    resetLayout = (By.XPATH, "//button[contains(text(),'Reset')]")
    resetOk = (By.XPATH,"//button[@role='button'][normalize-space()='OK']")
    factorySettings = (By.XPATH,"(//span[contains(text(),'Factory Setting')])[1]")
    filterTextArea = (By.XPATH, "//textarea[@class='o9-pivot-search-filter']")
    filterOK = (By.XPATH, "//button[contains(text(),'OK')][@class='slick-button okButton save']")
    currentdatefetch = (By.XPATH, "//td[@data-field='DisplayName']")
    layoutData = (By.XPATH,"//button[contains(text(),'Data')]")
    #Santhoshi =
    layoutReset = (By.XPATH, "//div[@class='button-bar']//button[@class='slick-button reset']")
    layoutResetOk = (By.XPATH, "//div[@class='k-widget k-window k-dialog']//button[contains(text(),'OK')]")
    layoutDataTab = (
    By.XPATH, "//div[@class='o9-pivot-layout-config k-window-content']//button[contains(text(),'Data')]")
    layoutDataSelectAll = (
    By.XPATH, "//div[@class='o9-pivot-layout-config k-window-content']//div[@id='dataPane']//*[contains(text(),'All')]//input")

    factorySettingSelect = (By.XPATH, "//div[@id='frozenColumns-list']//*[@data-offset-index='3']")

    addFilter = (By.XPATH, "//button[@title='Add Group']//span[contains(text(),'Value Filter')]")
    field1 = (By.XPATH, "//span[@title='Fields']/span/span")
    field2 = (By.XPATH, "//span[@title='Operators']/span/span")
    selectField2 = (By.XPATH, "//li[@tabindex='-1']//span[contains(text(),'does not equal blank')]")
    saveChanges = (By.XPATH, "//button[@name='MeasureValueFiltersSaveButton']")

    filterOk = (By.XPATH, "//div[@class='o9-pivot-filter-section-up-divider']//*[contains(text(),'OK')]")
    goBack = (By.ID, "GoBack")
    submitYes = (
    By.XPATH, "//div[@class='k-widget k-window k-display-inline-flex k-state-focused']//button[contains(text(),'Yes')]")
    filterSelectAll = (By.XPATH,
                       "//div[@class='ui-multiselect-menu ui-widget ui-widget-content ui-corner-all']//*[contains(text(),'(Select All)')]")
    filterSearch = (By.XPATH, "//div[@class='ui-multiselect-filter']/div[2]/textarea")
    filterFirstRecord = (
    By.XPATH, "//div[@class='ui-multiselect-menu ui-widget ui-widget-content ui-corner-all']/ul/li[2]/label/span")

    FavoriteNameInput = (By.XPATH, "//div[@class='name-field']//span//input")
    FavoriteDescInput = (By.XPATH, "//div[@class='description-field']//textarea")
    manageFavourite = (By.XPATH, "//span[contains(text(),'Manage Favorites')]")
    deleteThird = (
    By.XPATH, "//ul[@class='favListView favTable k-widget k-listview k-listview-bordered']//li[3]//*[@title='Delete']")
    howerThirdRow = (By.XPATH, "//li[@class='sortable selected k-listview-item']")
    closeManageFav = (By.XPATH,
                      "//div[@class='k-widget k-window k-display-inline-flex o9-curve-window k-state-focused']//a[@aria-label='Close']")
    chartLayoutButton = (By.XPATH, "//button[@title='Chart Layout']/i")
    chartLayoutSave = (By.XPATH, "//div[@class='o9-lc-display-items']//span[@id='lcLayoutSaveButton']")
    successmsg= (By.XPATH,"//*[contains(text(),'Request submitted successfully. Please wait for the notification.')]")




    def __init__(self, driver):
        self.driver = driver


    def getfilterTextArea(self):
        return self.driver.find_element(*StaticElements.filterTextArea)

    def getsuccessmsg(self):
        return self.driver.find_element(*StaticElements.successmsg)

    def getlayoutData(self):
        return self.driver.find_element(*StaticElements.layoutData)

    def getcurrentdatefetch(self):
        return self.driver.find_element(*StaticElements.currentdatefetch)

    def getfilterOK(self):
        return self.driver.find_element(*StaticElements.filterOK)

    def getsavebutton(self):
        return self.driver.find_element(*StaticElements.save)

    def getpopupSubmit(self):
        return self.driver.find_element(*StaticElements.popupSubmit)

    def getOk(self):
        return self.driver.find_element(*StaticElements.ok)

    def getpopupclose(self):
        return self.driver.find_element(*StaticElements.popupclose)

    def getDownloadButton(self):
        return self.driver.find_element(*StaticElements.DownloadButton)

    def getLayoutButton(self):
        return self.driver.find_element(*StaticElements.LayoutButton)

    def getFiltersButton(self):
        return self.driver.find_element(*StaticElements.FilterButton)

    def getFavoriteButton(self):
        return self.driver.find_element(*StaticElements.FavoriteButton)

    def getShareButton(self):
        return self.driver.find_element(*StaticElements.ShareButton)

    def getFavoriteName(self):
        return self.driver.find_element(*StaticElements.Favorite_Name)

    def getFavoriteDescription(self):
        return self.driver.find_element(*StaticElements.Favorite_Description)

    def getFavoriteSave(self):
        return self.driver.find_element(*StaticElements.Favorite_Save)

    def getFavoriteCancel(self):
        return self.driver.find_element(*StaticElements.Favorite_Cancel)

    def getShareName(self):
        return self.driver.find_element(*StaticElements.Share_Name)

    def getShareDescription(self):
        return self.driver.find_element(*StaticElements.Share_Description)

    def getShareSave(self):
        return self.driver.find_element(*StaticElements.Favorite_Save)

    def getShareCancel(self):
        return self.driver.find_element(*StaticElements.Favorite_Cancel)

    def getFilterIcon1(self):
        return self.driver.find_element(*StaticElements.filter_icon1)

    def getFilterIcon2(self):
        return self.driver.find_element(*StaticElements.filter_icon2)

    def getFilterIcon3(self):
        return self.driver.find_element(*StaticElements.filter_icon3)

    def getFilterIcon4(self):
        return self.driver.find_element(*StaticElements.filter_icon4)

    def getSaveButton(self):
        return self.driver.find_element(*StaticElements.SaveButton)

    def getDiscardButton(self):
        return self.driver.find_element(*StaticElements.DiscardButton)

    def getbellicon(self):
        return self.driver.find_element(*StaticElements.bellicon)

    def getdataverify(self):
        return self.driver.find_elements(*StaticElements.dataverify)

    def getexpand(self):
        return self.driver.find_element(*StaticElements.expand)

    def getthreedots(self):
        return self.driver.find_element(*StaticElements.threedots)

    def getDesignerSettings(self):
        return self.driver.find_element(*StaticElements.designerSettings)

    def getdesignerlayout(self):
        return self.driver.find_element(*StaticElements.designerlayout)

    def getclose(self):
        return self.driver.find_element(*StaticElements.close)

    def getallDept(self):
        return self.driver.find_element(*StaticElements.allDept)

    def getalldivison(self):
        return self.driver.find_element(*StaticElements.alldivison)

    def getallgrp(self):
        return self.driver.find_element(*StaticElements.allgrp)

    def getitemDept(self):
        return self.driver.find_element(*StaticElements.itemdept)

    def gettitleDept(self):
        return self.driver.find_element(*StaticElements.titledept)

    def getselectalldept(self):
        return self.driver.find_element(*StaticElements.selectalldept)

    def getselectallPeriod(self):
        return self.driver.find_element(*StaticElements.selectallPeriod)

    def getMnBottomWear(self):
        return self.driver.find_element(*StaticElements.MNbottomWear)

    def getkidsHome(self):
        return self.driver.find_element(*StaticElements.kidsHome)

    def getMNSoftAccessory(self):
        return self.driver.find_element(*StaticElements.MNSoftAccessory)

    def getapply(self):
        return self.driver.find_element(*StaticElements.apply)

    def getallItemCode(self):
        return self.driver.find_element(*StaticElements.allItemCode)

    def getclass(self):
        return self.driver.find_element(*StaticElements.classs)

    def getfilter1(self):
        return self.driver.find_element(*StaticElements.filter1)

    def getfilterelement1row1(self):
        return self.driver.find_element(*StaticElements.filterelement1row1)

    def getmonth(self):
        return self.driver.find_element(*StaticElements.month)

    def getcumulative(self):
        return self.driver.find_element(*StaticElements.cumulative)

    def getdesignLayout(self):
        return self.driver.find_element(*StaticElements.designLayout)

    def getviewReport(self):
        return self.driver.find_element(*StaticElements.viewReport)

    def geteditInDesigner(self):
        return self.driver.find_element(*StaticElements.editInDesigner)

    def getfilterAllYear(self):
        return self.driver.find_element(*StaticElements.filterAllYear)

    def getWeekFilter(self):
        return self.driver.find_element(*StaticElements.weekFilter)

    def getselectAllWeek(self):
        return self.driver.find_element(*StaticElements.selectAllWeek)

    def getexpandFilterDS(self):
        return self.driver.find_element(*StaticElements.expandFilter)

    def getcloseReportedMenu(self):
        return self.driver.find_element(*StaticElements.closeReportedMenu)

    def getFileImport(self):
        return self.driver.find_element(*StaticElements.fileImport)

    def getSelectFile(self):
        return self.driver.find_element(*StaticElements.selectFile)

    def getSelectWhole(self):
        return self.driver.find_element(*StaticElements.selectWhole)

    def getUpload(self):
        return self.driver.find_element(*StaticElements.upload)

    def getPopupOk(self):
        return self.driver.find_element(*StaticElements.popupOk)

    def getrefresh(self):
        return self.driver.find_element(*StaticElements.refresh)

    def getnotification(self):
        return self.driver.find_element(*StaticElements.notification)

    def getcloseupload(self):
        return self.driver.find_element(*StaticElements.closeupload)

    def getsaveLayout(self):
        return self.driver.find_element(*StaticElements.saveLayout)

    def getresetLayout(self):
        return self.driver.find_element(*StaticElements.resetLayout)

    def getResetOK(self):
        return self.driver.find_element(*StaticElements.resetOk)


    def getfactorySettings(self):
        return self.driver.find_element(*StaticElements.factorySettings)

    def getGoBack(self):
        return self.driver.find_element(*StaticElements.goBack)

    # To click on Any Global Action Button
    # Supply Name of action button as parameter
    def getGlobal_AB(self, AB_Name):
        return self.driver.find_element(By.XPATH, f"//header[@id='appHeader']//a[@name='{AB_Name}']/i")

    # To click on Any Report Action Button
    # Supply data_o9widgetname and Title of action button as 1st and 2nd parameter RESPECTIVELY
    def getReports_AB(self, data_o9widgetname, AB_Title):
        return self.driver.find_element(By.XPATH,
                                        f"//div[@data-o9widgetname='{data_o9widgetname}']//a[@title='{AB_Title}']//i")

    # To click on Any Page
    # Supply data_o9title of Page as parameter
    def getPage(self, data_o9title):
        return self.driver.find_element(By.XPATH, f"//div[@data-o9title='{data_o9title}']")


    def getclickbyName(self,Tag,Name):
        return self.driver.find_element(By.XPATH,
                                        f"//{Tag}[normalize-space()='{Name}']")


    # To click on Any View
    # Supply Inner_Text of View as parameter
    def getView(self, Inner_Text):
        return self.driver.find_element(By.XPATH,
                                        f"//a[@data-role='listview-link']//span[contains(text(),'{Inner_Text}')]/..")

    # To click on 1st checkbox of any report
    # Supply data_o9widgetname of report as parameter
    def getSelectFirstCheckbox(self, data_o9widgetname):
        return self.driver.find_element(By.XPATH,f"//div[@data-o9widgetname='{data_o9widgetname}']//div[@name='_r0c0']//label//span")


    def gettitle(self, title):
        return self.driver.find_element(By.XPATH,f"//a[@title='{title}']")

    def getlayoutbuttons(self, data_o9widgetname):
        return self.driver.find_element(By.XPATH,f"//div[@data-o9widgetname='{data_o9widgetname}']//button[contains(text(),'Layout')]")

    def getlayoutDataMeasures(self, i):
        return self.driver.find_element(By.XPATH,f"//div[@id='Measure_Members']//div[{i}]//span[@class='o9-pivot-layout-measure-name-element o9-pivot-layout-config-name-hidden']")

    def getData(self,i,j,data_o9widgetname):
        return self.driver.find_element(By.XPATH,f"//div[@data-o9widgetname='{data_o9widgetname}']//div[@name='_r{i}c{j}']")

    def getGraphData(self,i,data_o9widgetname):
        return self.driver.find_element(By.XPATH,f"//div[@data-o9widgetname='{data_o9widgetname}']//div[@data-template='horizontal-item-templ']//div[{i}]")

    def getLayoutReset(self):
        return self.driver.find_element(*StaticElements.layoutReset)

    def getLayoutResetOk(self):
        return self.driver.find_element(*StaticElements.layoutResetOk)

    def getLayoutDataTab(self):
        return self.driver.find_element(*StaticElements.layoutDataTab)

    def getLayoutDataSelectAll(self):
        return self.driver.find_element(*StaticElements.layoutDataSelectAll)

    def getfactorySettingSelect(self):
        return self.driver.find_element(*StaticElements.factorySettingSelect)

    def getAddFilter(self):
        return self.driver.find_element(*StaticElements.addFilter)

    def getField1(self):
        return self.driver.find_element(*StaticElements.field1)

    def getField2(self):
        return self.driver.find_element(*StaticElements.field2)

    def getSelectField2(self):
        return self.driver.find_element(*StaticElements.selectField2)

    def getSaveChanges(self):
        return self.driver.find_element(*StaticElements.saveChanges)

    def getFilterOk(self):
        return self.driver.find_element(*StaticElements.filterOk)

    def getSubmitYes(self):
        return self.driver.find_element(*StaticElements.submitYes)

    def getFilterSelectAll(self):
        return self.driver.find_element(*StaticElements.filterSelectAll)

    def getFilterSearch(self):
        return self.driver.find_element(*StaticElements.filterSearch)

    def getFilterFirstRecord(self):
        return self.driver.find_element(*StaticElements.filterFirstRecord)

    def getFavNameInput(self):
        return self.driver.find_element(*StaticElements.FavoriteNameInput)

    def getFavDescInput(self):
        return self.driver.find_element(*StaticElements.FavoriteDescInput)

    def getManageFavourite(self):
        return self.driver.find_element(*StaticElements.manageFavourite)

    def getDeleteThird(self):
        return self.driver.find_element(*StaticElements.deleteThird)

    def getHowerThirdRow(self):
        return self.driver.find_element(*StaticElements.howerThirdRow)

    def getCloseManageFav(self):
        return self.driver.find_element(*StaticElements.closeManageFav)

    def getChartLayoutButton(self):
        return self.driver.find_element(*StaticElements.chartLayoutButton)

    def getChartLayoutSave(self):
        return self.driver.find_element(*StaticElements.chartLayoutSave)










