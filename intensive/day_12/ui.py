from m3_ext.ui.containers import ExtFieldSet, ExtForm, ExtToolBar
from m3_ext.ui.controls import ExtButton
from m3_ext.ui.fields import ExtStringField, ExtHiddenField
from m3_ext.ui.panels import ExtObjectGrid
from m3_ext.ui.windows import ExtWindow, ExtEditWindow


class MasterPanel(ExtFieldSet):
    """
    Пример простой панели с кнопками и обработчиками
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Привет, Мир!'
        self.height = 200
        self.items.extend([
            ExtButton(
                text='Нажми меня',
                handler='''
                    function(){
                        const parent = this.ownerCt;
                        const strField = parent.findByType('textfield')[0];
                        sendRequest("/demo/win1", null, {"str_field": strField.getValue()});
                    }''',
            ),
            ExtStringField(
                label='Поле ввода',
                name='str_field',
            ),
            ExtButton(
                text='Grid',
                handler='function(){ sendRequest("/demo/gridwin");}',
            ),
        ])


class MasterWindow(ExtWindow):
    """
    Пример окна
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Вот и я!'
        self.str_field = ExtStringField(
            label='Поле ввода',
            name='str_field',
        )
        self.items.extend([
            self.str_field
        ])


class GridWindow(ExtWindow):
    """
    Пример окна с гридом
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Grid'
        self.layout = 'border'
        self.grid = ExtObjectGrid(
            region='center'
        )
        self.grid.plugins.append('new Ext.ux.grid.GridHeaderFilters()')
        self.grid.add_column(
            data_index='id',
            header='ИД',
        )
        self.grid.add_column(
            data_index='name',
            header='Имя',
            sortable=True
        )
        self.items.extend([
            self.grid
        ])


class ItemWindow(ExtEditWindow):
    """
    Пример окна редактирования
    """
    def __init__(self, *args, create_new=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Карточка элемента'
        self.id_field = ExtHiddenField(
            name='id',
        )
        self.name_field = ExtStringField(
            label='Наименование',
            name='name',
        )
        self.form = ExtForm()
        self.button_align = self.align_left
        self.save_button = ExtButton(
            text=u'Сохранить',
            handler='submitForm')
        self.cancel_button = ExtButton(
            text=u'Закрыть',
            handler='function(){win.close();}')

        self.footer_bar = ExtToolBar()
        self.footer_bar.items.extend([
            self.save_button,
            self.cancel_button,
        ])

        self.form.items.extend([
            self.id_field,
            self.name_field,
        ])

        self.init_component(*args, **kwargs)
