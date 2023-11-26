-- Check if the category table exists
SELECT name FROM sqlite_master WHERE type='table' AND name='category';

-- If the table exists, insert spending categories
INSERT INTO category (title, description) VALUES
    ('Haushalt', 'Alles rund ums Zuhause - von flauschigen Kissen bis hin zu High-Tech-Haushaltsgeräten.'),
    ('Mobilität', 'Von actionreichen Fahrradtouren bis zu aufregenden Autoreisen - hier geht es um Mobilität!'),
    ('Gesundheit', 'Investiere in dein Wohlbefinden - sei es durch köstliche Smoothies oder Sportausrüstung.'),
    ('Ferien', 'Plane deinen nächsten Traumurlaub oder schmiede Pläne für aufregende Ferienaktivitäten.'),
    ('Lebensmittel', 'Von kulinarischen Abenteuern bis zu wöchentlichen Lebensmitteleinkäufen - hier geht es um Essen!'),
    ('Unterhaltung', 'Entdecke die Welt der Unterhaltung - von Konzerten und Kinoabenden bis zu abenteuerlichen Ausflügen.');
-- Add more categories as needed