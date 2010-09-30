from pyidml.fields import *
from pyidml.models import Element, Properties
from stories import BaseTextElement

class ParagraphStyleGroup(Element):
    Self = StringField(required=True)
    Name = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class RootParagraphStyleGroup(ParagraphStyleGroup):
    pass
    

class ParagraphStyle(BaseTextElement):
    Imported = BooleanField()
    KeyboardShortcut = StringField()
    NextStyle = StringField()
    BasedOn = StringField()
    

# TODO: AllNestedStyles

class CharacterStyleGroup(Element):
    Self = StringField(required=True)
    Name = StringField()
    
    Properties = EmbeddedDocumentField(Properties)


class RootCharacterStyleGroup(CharacterStyleGroup):
    pass
    

class CharacterStyle(BaseTextElement):
    Name = StringField()
    Imported = BooleanField()
    KeyboardShortcut = StringField()
    NextStyle = StringField()
    BasedOn = StringField()
    

# TODO: TableStyles, CellStyles

class ObjectStyleGroup(Element):
    """
    Object styles in an InDesign document can be organized into object style 
    groups.
    """
    Self = StringField(required=True)
    Name = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class RootObjectStyleGroup(ObjectStyleGroup):
    pass
    

class ObjectStyleProperties(Properties):
    BasedOn = StringField()
    

class ObjectStyle(Element):
    """
    Just as you use paragraph and character styles to quickly format text, you 
    can use object styles to quickly format graphics and frames.
    
    Object styles include settings for stroke, color, transparency, drop 
    shadows, paragraph styles, text wrap, and more. You can assign different 
    transparency effects for the object, fill, stroke, and text. Use object 
    styles, rather than applying extensive local formatting, to format page 
    items.
    
    You can apply object styles to objects, groups, and frames (including text 
    frames). A style can either clear and replace all object settings or it can 
    replace only specific settings, leaving other settings unchanged. You 
    control which settings the style affects by including or excluding a 
    category of settings in the definition.
    """
    Self = StringField(required=True)
    Name = StringField(required=True)
    AppliedParagraphStyle = StringField()
    ApplyNextParagraphStyle = BooleanField()
    EnableFill = BooleanField()
    EnableStroke = BooleanField()
    EnableParagraphStyle = BooleanField()
    EnableTextFrameGeneralOptions = BooleanField()
    EnableTextFrameBaselineOptions = BooleanField()
    EnableStoryOptions = BooleanField()
    EnableTextWrapAndOthers = BooleanField()
    EnableAnchoredObjectOptions = BooleanField()
    CornerRadius = FloatField()
    FillColor = StringField()
    FillTint = FloatField()
    OverprintFill = BooleanField()
    StrokeWeight = FloatField()
    MiterLimit = FloatField()
    EndCap = StringField()
    EndJoin = StringField()
    StrokeType = StringField()
    LeftLineEnd = StringField()
    RightLineEnd = StringField()
    StrokeColor = StringField()
    StrokeTint = FloatField()
    OverprintStroke = BooleanField()
    GapColor = StringField()
    GapTint = FloatField()
    OverprintGap = BooleanField()
    StrokeAlignment = StringField()
    Nonprinting = BooleanField()
    GradientFillAngle = FloatField()
    GradientStrokeAngle = FloatField()
    StrokeCornerAdjustment = StringField()
    StrokeDashAndGap = SpaceSeparatedListField(FloatField())
    AppliedNamedGrid = StringField()
    KeyboardShortcut = SpaceSeparatedListField(IntField())
    TopLeftCornerOption = StringField()
    TopRightCornerOption = StringField()
    BottomLeftCornerOption = StringField()
    BottomRightCornerOption = StringField()
    TopLeftCornerRadius = FloatField()
    TopRightCornerRadius = FloatField()
    BottomLeftCornerRadius = FloatField()
    BottomRightCornerRadius = FloatField()
    EnableFrameFittingOptions = BooleanField()
    CornerOption = StringField()
    EnableStrokeAndCornerOptions = BooleanField()
    
    Properties = EmbeddedDocumentField(ObjectStyleProperties)
    

class BaseObjectStyleEffectsSettings(Element):
    """
    This contains attributes that enable (when set to true) or disable (when 
    false) sections of the <ObjectStyle>
    """
    EnableTransparency = BooleanField()
    EnableDropShadow = BooleanField()
    EnableFeather = BooleanField()
    EnableInnerShadow = BooleanField()
    EnableOuterGlow = BooleanField()
    EnableInnerGlow = BooleanField()
    EnableBevelEmboss = BooleanField()
    EnableSatin = BooleanField()
    EnableDirectionalFeather = BooleanField()
    EnableGradientFeather = BooleanField()
    

class ObjectStyleObjectEffectsCategorySettings(BaseObjectStyleEffectsSettings):
    pass
    

class ObjectStyleStrokeEffectsCategorySettings(BaseObjectStyleEffectsSettings):
    pass
    

class ObjectStyleFillEffectsCategorySettings(BaseObjectStyleEffectsSettings):
    pass
    

class ObjectStyleContentEffectsCategorySettings(BaseObjectStyleEffectsSettings):
    pass
    

# TODO: TOCStyle, TOCStyleEntry, 

class TrapPreset(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    DefaultTrapWidth = FloatField()
    BlackWidth = FloatField()
    TrapJoin = StringField()
    TrapEnd = StringField()
    ObjectsToImages = BooleanField()
    ImagesToImages = BooleanField()
    InternalImages = BooleanField()
    OneBitImages = BooleanField()
    ImagePlacement = StringField()
    StepThreshold = FloatField()
    BlackColorThreshold = FloatField()
    BlackDensity = FloatField()
    SlidingTrapThreshold = FloatField()
    ColorReduction = FloatField()
    
    Properties = EmbeddedDocumentField(Properties)
    


