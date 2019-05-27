#!/bin/python
import wx


class HelloFrame(wx.Frame):
    testDataTitre = ["titre 1", "titre 2", "titre 3"]
    testDataContenue = {
        "titre1": ["T1 : contenue 1", "T1 : contenue 2"],
        "titre2": ["T2 : contenue 1", "T1 : contenue 2"],
        "titre3": ["T3 : contenue 1", "T1 : contenue 2"],
    }

    def search_title(self):
        return self.testDataTitre

    def search_contenu_by_title(self, title=""):
        return self.testDataContenue[title.replace(" ", "")]

    def __init__(self, *args, **kw):
        # appel du constructeur parent
        super(HelloFrame, self).__init__(*args, **kw)

        self.listTitre = []
        self.listContenue = []

        # creation d'un panel -conteneur-
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        # Ajouter un texte dans le conteneur
        text = wx.StaticText(panel, label="Perform lecture/écriture dans un fichier")
        textTitle = wx.StaticText(panel, label="Choisir un titre :")
        textContenu = wx.StaticText(panel, label="Choisir le contenu :")

        # Ajouter un bouton
        self.btn = wx.Button(panel, -1, "Rechercher titre")

        # Ajouter les listes deroulantes dans le conteneur

        self.lstTitle = wx.Choice(panel)
        self.lstContenue = wx.Choice(panel)

        box.Add(text)
        box.Add(self.btn)
        box.Add(textTitle)
        box.Add(self.lstTitle)
        box.Add(textContenu)
        box.Add(self.lstContenue)

        panel.SetSizer(box)
        panel.Fit()

        self.Centre()
        # for fun :)
        self.CreateStatusBar()
        self.SetStatusText("Ainsi va la vie :)")
        self.Bind(wx.EVT_CHOICE, self.onListTitleChange, self.lstTitle)
        self.Bind(wx.EVT_BUTTON, self.onBoutonClick, self.btn)
        self.Show(True)

    def onListTitleChange(self, event):
        # on modifie la liste des contenue correspondant au titre sélectionné.
        self.lstContenue.Clear()
        self.lstContenue.AppendItems(self.search_contenu_by_title(event.GetEventObject().GetStringSelection()))

    def onBoutonClick(self, event):
        # on modifie la liste des titreé.
        self.lstTitle.Clear()
        self.lstTitle.AppendItems(self.search_title())


if __name__ == '__main__':
    app = wx.App()
    HelloFrame(None, title='Demo R/W file UI', size=(480, 640))
    app.MainLoop()
