import i18n


def load_translations():
    i18n.load_path.append('translations')
    i18n.set('filename_format', '{locale}.{format}')
    i18n.set('locale', 'uz')
    i18n.set('fallback', 'uz')
