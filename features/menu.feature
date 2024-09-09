Feature: Verify Cloud Home Page UI
    
    Scenario: Verify Menu Tabs
        Given Go to Demo page
        Then Verify number of menu tabs
        Then Verify information of menu tabs
    
    Scenario: Verify News Tabs
        Given Go to Demo page
        Then Verify number of news tabs
        Then Verify information of news tabs

    Scenario: Verify news in each News Tab
        Given Go to Demo page
        When View news in current News Tab
        Then Compare news in current Tab with different News Tabs

    Scenario: Click on `Docs` on Header
        Given Go to Demo page
        When Click on `Docs` header
        Then Verify if navigating to correct Documentation page
