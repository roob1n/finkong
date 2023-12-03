-- Check if the category table exists
SELECT name FROM sqlite_master WHERE type='table' AND name='category';

-- If the table exists, insert spending categories
INSERT INTO category (title, description, color) VALUES 
    ('Haushalt', 'Alles rund ums Zuhause - von flauschigen Kissen bis hin zu High-Tech-Haushaltsgeräten.', '#582f0e'),
    ('Mobilität', 'Von actionreichen Fahrradtouren bis zu aufregenden Autoreisen - hier geht es um Mobilität!', '#7f4f24'),
    ('Gesundheit', 'Investiere in dein Wohlbefinden - sei es durch köstliche Smoothies oder Sportausrüstung.', '#b6ad90'),
    ('Ferien', 'Plane deinen nächsten Traumurlaub oder schmiede Pläne für aufregende Ferienaktivitäten.', '#a68a64'), 
    ('Lebensmittel', 'Von kulinarischen Abenteuern bis zu wöchentlichen Lebensmitteleinkäufen - hier geht es um Essen!', '#656d4a'), 
    ('Unterhaltung', 'Entdecke die Welt der Unterhaltung - von Konzerten und Kinoabenden bis zu abenteuerlichen Ausflügen.', '#333d29');
-- Add more categories as needed